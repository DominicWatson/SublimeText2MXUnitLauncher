import sublime, sublime_plugin, webbrowser

class LaunchTestSuiteCommand(sublime_plugin.TextCommand):
    def run(self, args):
        s   = sublime.load_settings("MxUnit.sublime-settings")
        url = s.get('base_url', 'http://localhost') + s.get('test_suite', '/TestSuite.cfm')
        webbrowser.open(url)