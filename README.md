# DNS CLI

Do all the things about domain names from the command line!


## Adding/setting/removing A records

Add an A record:

    dnc add foo.okt.red 173.12.34.56

Note: this will not work if there is already a CNAME record.

It is possible to add multiple A records in one step:

    dnc add www.okt.red 173.12.34.56 173.23.45.67

Using `set` instead of `add` will replace existing records,
instead of appending to the existing list:

    dnc set www.okt.red 173.44.55.66

Of course, multiple records can be added this way:

    dnc set www.okt.red 173.55.66.77 173.99.88.77

The `-f` flag can be used to force removal of a `CNAME` record:

    dnc set -f www.okt.red 173.44.55.66

It is possible to remove a record:

    dnc rm www.okt.red 173.44.55.66


## `AAAA` records

They work exactly the same way. The program will automatically
detect that you want a `AAAA` record because of its format:

    dnc add foo.okt.red 2001:dead::f00d

It is possible to remove them the same way. It is also possible
to add or remove mixed type records:

    dnc rm foo.okt.red 2001:dead::f00d 173.44.55.66


## `rm -f`

When trying to remove a record that doesn't exist, an error
is thrown, except if the `-f` flag is specified:

    dnc rm -f nonexistend.okt.red 1.2.3.4


## Mass removal

It is possible to remove all records for a given name,
but then the `-f` option has to be given:

    dnc rm -f www.okt.red


## `CNAME` records

Easy: if something is neither `A` nor `AAAA`, it is a `CNAME`.

Example:

    dnc add secure.okt.red ssl.okt.red
    dnc rm -f secure.okt.red

Note that since there can only be one `CNAME` record at a time
(and no other record can co-exist with a `CNAME` record), `add`
and `set` are equivalent for this type of record.


## Other records

What about `TXT`, `HINFO`, `SRV`, etc.?

Since `TXT` and `HINFO` are just plain text, the type must be
explicitly specified:

    dnc add -t HINFO ssl.okt.red F16-HUGEIP-LOADBALANCER
    dnc rm -t HINFO ssl.okt.red

Note: when specifiying a type with `rm -t ...` without an
explicit record, it is not necessary to give `-f`.

`SRV` records can be specified using the following format:

    dnc add _xmpp._tcp.okt.red ejab.okt.red:5222@10

Where `5222` is the port number and `10` the priority.


## Listing existing records

Listing one specific name:

    $ dnc ls www.okt.red
    A 173.44.55.66
    A 173.55.66.77
    AAAA 2001:f00d::cafe
    HINFO APACHE-2-2-UBUNTU

Listing all names under something:

    $ dnc ls -r okt.red
    okt.red NS a.dns.gandi.net
    okt.red NS b.dns.gandi.net
    www.okt.red A 173.44.55.66

By default, don't show NS, MX, SOA, unless `-a` flag is given.
(Treat them as hidden files.)     

 


FIXME: TTL
