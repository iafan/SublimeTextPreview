About
=====

Preview is a Sublime Text 2 plugin that maps your local project files to URLs and opens them in your browser for preview.

Installation 
============

- Install 'Package Control', then search for 'Preview' and install

Initial setup
=============

Edit plugin settings (`Preferences > Package Settings > Preview > Settings — User`) and provide mapping rules, like this:

    {
        "rules": [
            // prohibit previewing local files (i.e. files that don't match any rule)
            {
                "url": ""
            },

            // allow opening local .htm and .html in browser
            {
                "path_suffix": ".htm",
                "url_prefix": "file:///"
            },
            {
                "path_suffix": ".html",
                "url_prefix": "file:///"
            },

            // sample website
            {
                // for all files matching the path_prefix, construct URL using url_prefix
                "path_prefix": "C:/Work/www/",
                "url_prefix": "http://localhost/",
                // append this string to all URLs
                "url_append": "?debug"
            },
            {
                // files in /inc/ subdirectory can't be previewed directly, so just open the root URL
                "path_prefix": "C:/Work/www/inc/",
                "url": "http://localhost/"
            },
            {
                // when editing .htaccess files, just open the containing folder
                "path_prefix": "C:/Work/www/inc/",
                "path_suffix": "/.htaccess",
                "url_prefix": "http://localhost/",
                "url_suffix": "/"
            }
        ]
    }

In addition to matching files by `path_prefix` and replacing this with `url_prefix`, you can also define `path_suffix` (for example, a file extension) and replace it with `url_suffix`. If `url_suffix` is not defined, then `path_suffix` will not be removed from a final URL.

In contrast to `url_suffix`, an optional `url_append` parameter allows to add some text to an end of the URL without having the matching `path_suffix` replaced.

`path_prefix` and `path_suffix` are case-sensitive. Mind the trailing slashes. Under Windows, you can use both `\\` and `/` as path delimiters.

Rules are applied top to bottom. If file path matches several rules, the last rule is used. You can use this to define mapping overrides.

Usage
=====

Pressing `F12` will map current file to an URL and open this URL in your default browser. If no rule is matched, the file
will be opened locally as `file:///...` in a program associated with this file extension (not necessarily a browser).

Version 1.0
===========

Initial release