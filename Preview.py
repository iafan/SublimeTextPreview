import sublime, sublime_plugin
import webbrowser, pprint, re

settings = None

class PreviewCommand(sublime_plugin.TextCommand):   

    def is_enabled(self):
        # if this view has no file name associated (untitled file), disable the command
        return self.view.file_name() != None

    def run(self, edit):
        global settings

        # load settings
        if settings == None:
            print("Preview: Loading settings")
            settings = sublime.load_settings('Preview.sublime-settings')

        if settings.get('rules') == None:
            print("Preview: No 'rules' section found in plugin settings")
            return

        # save file if it is dirty
        if self.view.is_dirty():
            self.view.run_command('save')

        # generate default file:/// URL
        fname = self.view.file_name().replace("\\", "/").replace(" ", "%20")
        url = "file:///" + fname

        # iterate through the rules
        for rule in settings.get('rules'):
            ok = True
            prefix_len = 0
            suffix_len = 0

            # test if path matches the path_prefix (if defined)
            if ok and 'path_prefix' in rule: 
                prefix = rule['path_prefix'].replace("\\", "/").replace(" ", "%20")
                prefix_len = len(prefix)
                ok = fname[:prefix_len] == prefix

            # test if path matches the path_suffix (if defined)
            if ok and 'path_suffix' in rule: 
                suffix = rule['path_suffix'].replace("\\", "/").replace(" ", "%20")
                suffix_len = len(suffix)
                ok = fname[-suffix_len:] == suffix

            # if rules match, construct the URL
            if ok:
                url = fname

                # replace first prefix_len symbols with url_prefix, if defined
                if 'url_prefix' in rule:
                    url = rule['url_prefix'] + url[prefix_len:]

                # replace last suffix_len symbols with url_suffix, if defined
                if 'url_suffix' in rule:
                    url = url[:-suffix_len] + rule['url_suffix']

                # append url_append, if defined
                if 'url_append' in rule:
                    url = url + rule['url_append']

                # if url is defined, use it as is
                if 'url' in rule:
                    url = rule['url']

        # if URL is not empty, open it in an associated application
        if url:
            print("Preview: " + url)
            webbrowser.open_new_tab(url)
        else:
            print("Preview: No matching rules found, nothing to do")
