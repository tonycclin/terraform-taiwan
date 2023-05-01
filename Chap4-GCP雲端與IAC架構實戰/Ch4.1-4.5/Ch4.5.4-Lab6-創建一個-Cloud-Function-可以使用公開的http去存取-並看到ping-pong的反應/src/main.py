from flask import Flask, request, make_response


def handler(request):
    headers = {
        'Content-Type': 'text/plain'
    }
    response = make_response('Hello, World!', 200, headers)
    return response


def ping(request):
    headers = {
        'Content-Type': 'text/plain'
    }
    response = make_response('Pong!', 200, headers)
    return response
