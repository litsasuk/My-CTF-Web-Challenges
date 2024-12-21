# python 3.12
import ast
import os

from flask import Flask, render_template, request, jsonify
BLACK_LIST = ['\'', '\"', '(', ')']
app = Flask(__name__)


attributes = {
    'Import': False,
    'ImportFrom': False,
    'alias': False,
    'BoolOp': ['values'],
    'BinOp': ['left', 'right'],
    'UnaryOp': ['operand'],
    'Lambda': ['body'],
    'IfExp': ['test', 'body', 'orelse'],
    'Dict': ['keys', 'values'],
    'Set': ['elts'],
    'ListComp': ['elt', 'generators'],
    'SetComp': ['elt', 'generators'],
    'DictComp': ['key', 'value', 'generators'],
    'GeneratorExp': ['elt', 'generators'],
    'Yield': ['value'],
    'Compare': ['left', 'comparators'],
    'Call': False,
    'Repr': ['value'],
    'Num': True,
    'Str': True,
    'Attribute': True,
    'Subscript': ['value'],
    'Name': True,
    'List': ['elts'],
    'Tuple': ['elts'],
    'Expr': ['value'],
    'comprehension': ['target', 'iter', 'ifs'],
}
def check_ast(m):
    for node in ast.walk(m):
        node_type = type(node).__name__
        if attributes.get(node_type, True) is False:
            return False
    return True

def check(code):
    for keyword in BLACK_LIST:
        if keyword in code.lower():
            return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_code():
    source_code = request.form.get('code', '')
    try:
        tree = compile(source_code, "<string>", 'exec', flags=ast.PyCF_ONLY_AST)
        if not check_ast(tree) or not check(source_code):
            return jsonify({"error": "Invalid or unsafe code."})
        safe_globals = {
            '__builtins__': {
                'pow': pow, 'divmod': divmod, 'min': min,
                'max': max, 'sum': sum, 'complex': complex,
                'oct': oct, 'hex': hex
            }
        }
        local_scope = {}
        exec(source_code, safe_globals, local_scope)
        return jsonify({"result": local_scope.get('a', None)})

    except Exception as e:
        return jsonify({"error": f"{str(e)}"})
if __name__ == '__main__':
    app.run()

