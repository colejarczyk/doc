Varnish
=======

`Varnish Cache <https://varnish-cache.org/>`_ is a web application accelerator also known as a caching HTTP reverse proxy.
Varnish speeds up responses from the server tremendously and helps improving performance of OpenLoyalty for clients who are
going to run OpenLoyalty for huge number of customers. Idea is simple. Backend application sends cache headers and based
on those, Varnish executes cache actions.

Technical details
-----------------

Open Loyalty uses `FOSHttpCacheBundle <https://github.com/FriendsOfSymfony/FOSHttpCacheBundle>`_ in order to integrate Varnish
with OpenLoyalty as a proxy client. Additionally this library use `FOSHttpCache <https://github.com/FriendsOfSymfony/FOSHttpCache>`_
which is responsible for controlling cache headers passed to proxy clients and invalidating cached objects.

Varnish is the first layer for the network traffic (after tool responsible for resolving HTTPS) and listening on 80 port.
Each request is passed to Varnish and then, if needed, forwarded to backend application (in order to refresh cache). Varnish is
very advanced and each operation flow can be managed by providing configuration files (Vcl files are located in docker/base/varnish).
Open Loyalty provides default configuration which is compatible with used Symfony bundles, but you can adjust it to your own needs.

Second place where http cache can be configured is symfony configuration. The dev/http_cache.yml file is used
for developer mode (disable cache) and prod/http_cache.yml contains simple configuration caches for several
endpoints. This file can be expanded according to `FOSHttpCacheBundle documentation <https://foshttpcachebundle.readthedocs.io/en/latest/reference.html>`_

The last place is `parameters.yaml` where you can find keys below:

`varnish_host` - host on which Varnish is listening (port can be added to host)
`http_cache_default_ttl` - time to live (for objects cached in proxy client).
`http_cache_invalidation` - indicates whether invalidation feature is enabled. If it is disabled then cache will be
expired only after TTL time.
`http_cache_base_url` - host which is main gateway for user's OpenLoyalty.
`http_cache_debug_headers` - indicates whether backend and Varnish should add debug headers to responses. It helps to
identify that page was cached or fetched from backend.

Enabling Varnish
----------------

By default Varnish is enabled on production mode (if you use our docker files), but `http_cache_default_ttl` value
in `parameters.yml` should be increased to higher value and `http_cache_invalidation` should be enabled. Make sure that
traffic is passed to Varnish on 80 port.

If you want to use external Varnish services (like Varnish on AWS) you should configure it using our VCL configuration
and forward traffic to Varnish.
