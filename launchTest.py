import sublime, sublime_plugin, webbrowser

class LaunchTestCommand(sublime_plugin.TextCommand):
    def run(self, args):
        s        = sublime.load_settings("MxUnit.sublime-settings")
        baseUrl  = s.get('base_url', 'http://localhost')
        basePath = s.get('base_path', '')
        context  = self.view.file_name().replace(basePath, "").replace("\\","/")
        fullUrl  = baseUrl + context + "?method=runTestRemote&format=html"

        webbrowser.open(fullUrl)