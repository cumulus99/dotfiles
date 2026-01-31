config.load_autoconfig()

config.bind = (",m", "spawn --detach mpv {url}") 
config.bind = (",C", "spawn --verbose --detach rm -R ~/.cache/qutebrowser")
c.tabs.padding = {'top':6, 'bottom':6, 'left':8, 'right':8}
c.url.default_page = "https://duckduckgo.com/"
c.url.start_pages = ["https://duckduckgo.com/"]
c.url.searchengines = {
        "DEFAULT": "https://duckduckgo.com/?q={}",
        "!aw": "https://wiki.archlinux.org/?search={}",
        "!dwn": "https://downdetector.com/search/?q={}",
        "!sspres": "https://sprites.spriters-resource.com/browse/?name={}",
        "!mspres": "https://models.spriters-resource.com/browse/?name={}"}

c.content.pdfjs = True
c.content.webgl = True
c.content.autoplay = True
c.content.blocking.enabled = True
c.completion.web_history.max_items = 0
c.completion.cmd_history_max_items = 0
c.content.geolocation = False
c.backend = 'webengine'
c.confirm_quit = ['multiple-tabs']

# dark mode
c.colors.webpage.preferred_color_scheme = 'light'
#c.colors.webpage.preferred_color_scheme = 'dark'
#c.colors.webpage.darkmode.enabled = True
#c.colors.webpage.darkmode.policy.images = 'never'
#c.colors.webpage.darkmode.policy.page = 'smart'
#c.colors.webpage.darkmode.algorithm = 'lightness-hsl'
#c.colors.webpage.bg = '#121b25'
c.colors.webpage.bg = '#FFFFFF'

c.downloads.location.directory = '~/Downloads'

c.content.blocking.enabled = True
c.content.blocking.method = 'both'
c.content.blocking.adblock.lists = [
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2022.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2023.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2024.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-cookies.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-others.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/quick-fixes.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt"]
