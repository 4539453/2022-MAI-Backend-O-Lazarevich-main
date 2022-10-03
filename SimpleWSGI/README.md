# Simple WSGI

![web_app](https://miro.medium.com/max/720/1*i_9gtKakG2QjgwXdFDdwRA.jpeg)

- Установить nginx и gunicorn;
- Настроить nginx для отдачи статический файлов из public/;
- Создать простейшее WSGI-приложение и запустить его с помощью gunicorn;
- Настроить проксирование запросов на nginx;
- Измерить производительность nginx и gunicorn c помощью ab или wrk.

## URI

**URI** — Uniform Resource Identifier

![URI_syntax_diagram](https://upload.wikimedia.org/wikipedia/commons/d/d6/URI_syntax_diagram.svg)

**URL** — Uniform Resource Locator

Specific type of URI is a reference to a web resource that specifies
its location on a computer network and a mechanism for retrieving it
(https, ftp, …).

**URN** — Uniform Resource Name

![URN_syntax_diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/URN_syntax_diagram_-_namestring.png/800px-URN_syntax_diagram_-_namestring.png)

`urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66`

---

[wiki/URI](https://en.wikipedia.org/wiki/URL)

[wiki/URN](https://en.wikipedia.org/wiki/Uniform_Resource_Name)

## An Application Server vs. a Web Server

A web server‘s fundamental job is to accept and fulfill requests from clients
for static content from a website (HTML pages, files, images, video, and so on).
The client is almost always a browser or mobile application and the request
takes the form of a Hypertext Transfer Protocol (HTTP) message, as does the
web server’s response.

An application server’s fundamental job is to provide its clients with access to
what is commonly called business logic, which generates dynamic content;
that is, it’s code that transforms data to provide the specialized functionality
offered by a business, service, or application. An application server’s clients
are often applications themselves, and can include web servers and
other application servers. Communication between the application server and
its clients might take the form of HTTP messages, but that is not required as
it is for communication between web servers and their clients.
Many other protocols are popular, including the variants of CGI.

<!-- https://www.nginx.com/resources/glossary/application-server-vs-web-server/ -->

---

[yt/Web Server vs Application Server](https://youtu.be/BcmUOmvl1N8)

[nginx/What Is an Application Server vs. a Web Server?](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)

## Gunicorn

WSGI basically provides bridge of your need to communicate between your Web Server and Web Application. WSGI (Web Server Gateway Interface), is a set of rules which allow a WSGI compliant server to work with a WSGI compliant Python application. WSGI also handles scaling for web servers to be able to handle thousands of requests so you don’t have to think about accepting multiple requests at a time.

Gunicorn is one implementation of a WSGI server for Python applications.

Gunicorn is a WSGI compliant web server for Python Applications that receive requests sent to the Web Server from a Client and forwards them onto the Python applications or Web Frameworks (such as Flask or Django) in order to run the appropriate application code for the request.

<!-- https://medium.com/@serdarilarslan/what-is-gunicorn-5e674fff131b -->

```bash
# WSGI_APP is optional if it is defined in a config file
set WSGI_APP $(MODULE_NAME):$(VARIABLE_NAME)
gunicorn [OPTIONS] [WSGI_APP]
```

---

[gunicorn/Running Gunicorn](https://docs.gunicorn.org/en/stable/run.html)

[lectureswww/wsgi](https://lectureswww.readthedocs.io/5.web.server/wsgi.html)

[medium/what-is-gunicorn](https://medium.com/@serdarilarslan/what-is-gunicorn-5e674fff131b)

[gunicorn/run](https://docs.gunicorn.org/en/stable/run.html)

## Nginx

[nginx/beginners_guide](https://nginx.org/en/docs/beginners_guide.html)

[nginx/ngx_http_upstream_module](https://nginx.org/en/docs/http/ngx_http_upstream_module.html)

## Benchmarks

```bash
# nginx -> static files
$ wrk -t12 -c400 -d30s http://192.168.122.108/data/
Running 30s test @ http://192.168.122.108/data/
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   167.95ms   65.05ms   1.97s    89.62%
    Req/Sec   151.42    103.54   780.00     63.84%
  35007 requests in 30.08s, 22.07MB read
  Socket errors: connect 0, read 0, write 0, timeout 334
Requests/sec:   1163.83
Transfer/sec:    751.22KB

$ wrk -t12 -c100 -d30s http://192.168.122.108/data/
Running 30s test @ http://192.168.122.108/data/
  12 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    88.46ms  107.26ms   1.98s    97.85%
    Req/Sec   105.03     28.37   363.00     83.56%
  37145 requests in 30.10s, 23.41MB read
Requests/sec:   1234.08
Transfer/sec:    796.56KB
```

```bash
# gunicorn -> backend
$ wrk -t12 -c400 -d30s http://192.168.122.108:8000
Running 30s test @ http://192.168.122.108:8000
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    91.01ms   13.91ms 254.34ms   93.87%
    Req/Sec   365.45     84.80     0.96k    83.41%
  130635 requests in 30.09s, 18.56MB read
Requests/sec:   4341.10
Transfer/sec:    631.67KB
```

```bash
# nginx reverse proxy -> gunicorn -> backend
$ wrk -t12 -c400 -d30s http://192.168.122.108/backend/
Running 30s test @ http://192.168.122.108/backend/
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   139.43ms   33.27ms 290.51ms   87.29%
    Req/Sec   244.28    104.57     1.25k    80.11%
  85145 requests in 30.10s, 12.91MB read
  Socket errors: connect 0, read 141, write 0, timeout 0
Requests/sec:   2829.08
Transfer/sec:    439.15KB

$ wrk -t12 -c200 -d30s http://192.168.122.108/backend/
Running 30s test @ http://192.168.122.108/backend/
  12 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    58.35ms    4.43ms 101.15ms   89.26%
    Req/Sec   275.15     55.67     0.87k    78.48%
  98743 requests in 30.10s, 14.97MB read
Requests/sec:   3280.53
Transfer/sec:    509.22KB
```
