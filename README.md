# python-demo

python demo for deployment tool

## Intro

This project includes demos of deploying python services with [jkom-cloud/deployment](https://github.com/jkom-cloud/deployment).

Please refer to chi.liu@jiukangyun.com for any question. Contribution to demo features/services are always welcomed!

## Usage

To use the auto-deployment service, `run.sh` must be provided in the root directory.
A process running this script will be initiated and managed by `PM2` daemon.

The following sections provide specs of python-based services deployed by the deployment tool.

## flask_demo

A simple web service via flask

- [/](http://precisecare.99jkom.com:5000): welcome
- [/ping](http://precisecare.99jkom.com:5000/ping): pong!
- [/fib/n](http://precisecare.99jkom.com:5000/fib/10): Fibonacci sequence of [F0...Fn]
