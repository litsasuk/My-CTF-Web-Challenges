<?php
function waf($request): int
{
    if (preg_match('/(input|data|stdin)/i', $request)) {
        die("no!");
    }
    return 1;
}