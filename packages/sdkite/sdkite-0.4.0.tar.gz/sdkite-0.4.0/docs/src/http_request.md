# HTTP Request

## HTTP method

The first parameter of the `request` method of an HTTP adapter allows to specify the
HTTP method to be used.

The HTTP adapter provides syntactic sugar for regular HTTP methods: `get`, `options`,
`head`, `post`, `put`, `patch`, `delete`.

## URL

The URL will be computed from:

- The `url` attribute of the `HTTPAdapterSpec` of each client
- The `url` argument passed to the `request` method (or `get`, `post`, etc.)

The rules used for combining URLs are quite flexible, and allow for the most frequent
use cases:

- Appending to the URL (a `/` separator will be used)
- Keeping only the base URL by using an absolute path (starting with `/`)
- Replacing the URL entirely by specifying an other URL

## Body

The `body` and `body_encoding` decide the data that will be sent in the body of the
request.

Here are the possible values for `body_encoding`:

`HTTPBodyEncoding.AUTO`

: Some heuristics are used to determine which encoding to use.

`HTTPBodyEncoding.NONE`

: Only basic types such as `bytes` and `str` are allowed, and will be passed
transparently.

`HTTPBodyEncoding.JSON`

: Data will be JSON-encoded.

`HTTPBodyEncoding.URLENCODE`

: Only works for `dict` types; keys and values will be urlencoded like a query string.

`HTTPBodyEncoding.MULTIPART`

: Only works for `dict` types; all values are encoded as if they were file data.

## Headers

The headers will be computed from:

- The `headers` attribute of the `HTTPAdapterSpec` of each client
- The `headers` argument passed to the `request` method (or `get`, `post`, etc.)

The later values override the former ones, in a case-insensitive manner.

!!! Note

    Depending on the `body_encoding` value, a `content-type` header may be automatically
    added.

## Stream mode

To ask the server to stream the response, set the `stream_response` parameter to `True`.

It is then recommended to use the `data_stream` attribute of
[the response object](http_response.md).

## Retry options

If an exception is raised when performing the request, 2 more attempts will be made with
some wait time between them.

This can be customized by passing some arguments:

- `retry_nb_attempts` to specify the total number of attempts (defaults to 3 attempts)
- `retry_wait_initial`, `retry_wait_max` and `retry_wait_jitter` allow to specify the
  exponential backoff parameters for the retry (they default to 1s, 60s and 1s
  respectively)

Finally, a `retry_callback` can be passed to be notified when a retry is performed. This
can be used for logging purposes for instance.

All these parameters can be specified (by order of precedence):

- When calling a request method (or get, post, etc.)
- On the HTTPAdapterSpec of each client
