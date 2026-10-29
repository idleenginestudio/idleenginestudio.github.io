# Builds the privacy policy pages (one folder per app) for https://idleenginestudio.github.io/privacy/
import os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'privacy')
DATE = '2026-10-29'
DEV = 'Idle Engine Studio'
CONTACT = 'mailto:idleenginestudio@gmail.com'
GOOGLE_PARTNER = 'https://policies.google.com/technologies/partner-sites'
GOOGLE_PRIVACY = 'https://policies.google.com/privacy'
GOOGLE_ADS_SETTINGS = 'https://myadcenter.google.com/'

CSS = """:root{--bg:#fbfaf7;--fg:#22252a;--mute:#5d636b;--line:#e3e0d8;--accent:#c4362b;--card:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#16181c;--fg:#e9e7e2;--mute:#a3a8b0;--line:#30343a;--accent:#ff7a6b;--card:#1e2126}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.75 -apple-system,BlinkMacSystemFont,"PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif}
main{max-width:760px;margin:0 auto;padding:32px 16px 64px}
h1{font-size:1.7rem;line-height:1.3;margin:0 0 4px}h2{font-size:1.15rem;margin:32px 0 8px;padding-top:8px;border-top:1px solid var(--line)}
h3{font-size:1rem;margin:20px 0 4px}p,li{margin:6px 0}ul{padding-left:1.3em}
.meta{color:var(--mute);font-size:.9rem;margin:0 0 20px}a{color:var(--accent)}
.lang{display:flex;gap:12px;font-size:.9rem;margin:0 0 24px}.en{margin-top:48px}
.apps{list-style:none;padding:0}.apps li{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:10px 0}
.apps small{display:block;color:var(--mute)}footer{margin-top:48px;color:var(--mute);font-size:.85rem}"""


def page(title, body):
    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="../style.css">\n<link rel="icon" type="image/png" href="/img/favicon-32.png">
</head>
<body><main>
{body}
<footer>{DEV} · <a href="../">所有 App 的隱私權政策</a> · <a href="../../">工作室首頁</a></footer>
</main></body>
</html>
"""


# ---------------------------------------------------------------- shared sections
def zh_ads(units):
    return f"""<h2>廣告（Google AdMob）</h2>
<p>這個 App 用 Google AdMob 顯示{units}。為了顯示廣告、計算成效、限制同一則廣告出現的次數和防止詐騙，Google 可能會收集並使用：</p>
<ul>
<li>裝置的廣告 ID（Android 廣告 ID）</li>
<li>IP 位址，以及由 IP 推算的大略位置（國家、城市）</li>
<li>裝置和系統資訊（機型、作業系統版本、語言）</li>
<li>你和廣告的互動（看了哪則廣告、有沒有點擊）以及當機紀錄</li>
</ul>
<p>在歐洲經濟區、英國和瑞士，第一次開啟 App 時會先看到 Google 的同意視窗，你可以選擇是否同意 Google 為個人化廣告使用你的資料；不同意時仍可能看到非個人化廣告。想重新選擇，可以在 Android 的「設定 → 應用程式」清除這個 App 的資料，下次開啟時會再出現同意視窗。</p>
<p>你也可以在 Android 的「設定 → Google → 廣告」重設或刪除廣告 ID，或到 <a href="{GOOGLE_ADS_SETTINGS}">Google 我的廣告中心</a>關閉個人化廣告。Google 怎麼使用這些資料：<a href="{GOOGLE_PARTNER}">Google 如何使用合作夥伴網站或應用程式的資料</a>、<a href="{GOOGLE_PRIVACY}">Google 隱私權政策</a>。</p>
"""


def en_ads(units):
    return f"""<h3>Ads (Google AdMob)</h3>
<p>The app shows {units} through Google AdMob. To serve and measure ads, cap how often an ad appears and prevent fraud, Google may collect and use your device's advertising ID, your IP address and the approximate location derived from it, device and system information, your interactions with ads, and crash data.</p>
<p>In the European Economic Area, the UK and Switzerland you first see Google's consent form and choose whether Google may use your data for personalised ads; without consent you may still see non-personalised ads. To choose again, clear the app's data in Android Settings → Apps and the form appears on the next launch. You can reset or delete your advertising ID in Android Settings → Google → Ads, or turn off personalised ads in <a href="{GOOGLE_ADS_SETTINGS}">My Ad Center</a>. See <a href="{GOOGLE_PARTNER}">How Google uses information from sites or apps that use its services</a> and the <a href="{GOOGLE_PRIVACY}">Google Privacy Policy</a>.</p>
"""


ZH_PURCHASE = """<h2>購買「移除廣告」</h2>
<p>購買由 Google Play 處理，付款資料只會交給 Google，我們看不到你的信用卡或帳號資料，只會收到「這台裝置已購買」的確認，用來關掉插頁廣告。</p>
"""
EN_PURCHASE = """<h3>The remove-ads purchase</h3>
<p>Purchases are handled by Google Play. Your payment details go to Google only; we never see your card or account details, only a confirmation that the purchase was made, which turns off the interstitial ads.</p>
"""


def zh_common_tail(extra_share=''):
    return f"""<h2>資料分享</h2>
<p>我們不會出售你的資料。除了上面提到的 Google 服務{extra_share}，我們不會把資料提供給其他人，除非法律要求。</p>
<h2>兒童</h2>
<p>這個 App 不是以 13 歲以下兒童為主要對象，我們也不會刻意收集兒童的個人資料。如果你認為孩子提供了個人資料給我們，請聯絡我們，我們會刪除。</p>
<h2>你的權利</h2>
<p>你可以要求查看、更正或刪除與你有關的資料，也可以撤回同意。請透過下面的聯絡方式告訴我們。Google 收集的廣告資料，請用上面 Google 提供的設定管理。</p>
<h2>政策變更</h2>
<p>如果這份政策有變更，我們會更新這一頁和上面的日期。</p>
<h2>聯絡我們</h2>
<p>開發者：{DEV}<br>電子郵件：<a href="{CONTACT}">idleenginestudio@gmail.com</a></p>
"""


def en_common_tail(extra_share=''):
    return f"""<h3>Sharing</h3>
<p>We do not sell your data. Apart from the Google services above{extra_share}, we do not share data with anyone unless the law requires it.</p>
<h3>Children</h3>
<p>The app is not directed at children under 13, and we do not knowingly collect personal information from children. If you believe a child has given us personal information, contact us and we will delete it.</p>
<h3>Your rights</h3>
<p>You may ask to access, correct or delete data about you, or withdraw consent, by contacting us. Advertising data collected by Google is managed through Google's settings linked above.</p>
<h3>Changes</h3>
<p>If this policy changes, we will update this page and the date above.</p>
<h3>Contact</h3>
<p>Developer: {DEV}. Email: <a href="{CONTACT}">idleenginestudio@gmail.com</a>.</p>
"""


def head(zh_name, en_name):
    return f"""<h1>{zh_name} 隱私權政策</h1>
<p class="meta">{en_name} Privacy Policy · 生效日期 Effective {DATE}</p>
<p class="lang"><a href="#zh">中文</a><a href="#en">English</a></p>
"""


# ---------------------------------------------------------------- apps
APPS = []

APPS.append(dict(
    slug='match-architect', zh='火柴建築師', en='Match Architect',
    desc='用火柴搭建築、撐過地震的益智遊戲（Android、網頁、Steam）',
    body=head('火柴建築師', 'Match Architect') + f"""<section id="zh">
<p>{DEV}（以下稱「我們」）開發的《火柴建築師》有 Android App、網頁版和 Steam 版。這份政策說明各版本會處理哪些資料。</p>
<h2>我們自己不收集個人資料</h2>
<p>遊戲不需要註冊或登入。關卡進度、金幣、商店道具和設定都只存在你的裝置（瀏覽器或 App 的本機儲存空間）裡，不會傳到我們的伺服器。刪除 App 或清除瀏覽器資料就會一起刪除。</p>
<h2>各版本</h2>
<ul>
<li><b>Android App</b>：有廣告和「移除廣告」購買，見下方說明。</li>
<li><b>網頁版</b>（itch.io 等網頁遊戲平台）：沒有廣告，我們不收集資料。網頁版會從 Google Fonts 載入字型，載入時你的瀏覽器會把 IP 位址等連線資訊傳給 Google；遊戲所在的平台（例如 itch.io）也有自己的隱私權政策。</li>
<li><b>Claude 分享連結版</b>：有排行榜。你上榜時會把暱稱、每關最少火柴數和金幣總數存到這個頁面的共用資料庫，其他玩家看得到；資料由 Anthropic 的 Claude 服務保存。</li>
<li><b>Steam 版</b>：買斷，沒有廣告也沒有內購；購買和帳號由 Steam（Valve）處理。</li>
</ul>
""" + zh_ads('獎勵廣告（由你選擇觀看，換取遊戲內獎勵）和插頁廣告（委託之間）') + ZH_PURCHASE + zh_common_tail('，以及 Claude 分享連結版的排行榜') + f"""</section>
<section id="en" class="en">
<h2>English</h2>
<p>Match Architect by {DEV} ("we") comes as an Android app, a web version and a Steam version. This policy explains what data each one handles.</p>
<h3>We collect no personal data ourselves</h3>
<p>There is no sign-up or login. Progress, coins, items and settings are stored only on your device (the browser's or the app's local storage) and never sent to our servers. Uninstalling the app or clearing browser data deletes them.</p>
<h3>Versions</h3>
<ul>
<li><b>Android app</b>: ads and a remove-ads purchase, described below.</li>
<li><b>Web version</b> (itch.io and other web game portals): no ads, and we collect no data. It loads fonts from Google Fonts, so your browser sends connection information such as your IP address to Google; the portal hosting the game (for example itch.io) has its own privacy policy.</li>
<li><b>Claude shared-link version</b>: has leaderboards. When you post a score, your nickname, best match counts and coin total are saved in the page's shared database, visible to other players and stored by Anthropic's Claude service.</li>
<li><b>Steam version</b>: paid up front, no ads, no in-app purchases; purchase and account are handled by Steam (Valve).</li>
</ul>
""" + en_ads('rewarded ads (which you choose to watch for an in-game reward) and interstitial ads (between jobs)') + EN_PURCHASE + en_common_tail(' and the leaderboard of the Claude shared-link version') + "</section>"))

APPS.append(dict(
    slug='mahjong-three-kingdoms', zh='麻將三國戰', en='Mahjong Three Kingdoms',
    desc='台灣十六張麻將 × 三國塔防（Android）',
    body=head('麻將三國戰', 'Mahjong Three Kingdoms') + f"""<section id="zh">
<p>{DEV}（以下稱「我們」）開發的《麻將三國戰》Android App。這份政策說明 App 會處理哪些資料。</p>
<h2>我們自己不收集個人資料</h2>
<p>遊戲不需要註冊或登入。關卡進度、金幣、武將和設定只存在你的裝置裡，不會傳到我們的伺服器。刪除 App 就會一起刪除。</p>
""" + zh_ads('插頁廣告（每隔幾場戰鬥，在結算畫面離開時）和獎勵廣告（由你選擇觀看，金幣加倍）') + ZH_PURCHASE + zh_common_tail() + f"""</section>
<section id="en" class="en">
<h2>English</h2>
<p>This policy covers the Mahjong Three Kingdoms Android app by {DEV} ("we").</p>
<h3>We collect no personal data ourselves</h3>
<p>There is no sign-up or login. Progress, coins, heroes and settings are stored only on your device and never sent to our servers. Uninstalling the app deletes them.</p>
""" + en_ads('interstitial ads (every few battles, when you leave the result screen) and rewarded ads (which you choose to watch to double your coins)') + EN_PURCHASE + en_common_tail() + "</section>"))

APPS.append(dict(
    slug='qiyun-avengers', zh='氣運復仇者', en='QiYun Avengers',
    desc='短局制 2D 動作遊戲（Android，開發中）',
    body=head('氣運復仇者', 'QiYun Avengers') + f"""<section id="zh">
<p>{DEV}（以下稱「我們」）開發的《氣運復仇者》Android App。這份政策說明 App 會處理哪些資料。</p>
<h2>我們自己不收集個人資料</h2>
<p>遊戲不需要註冊或登入。進度和設定只存在你的裝置裡，不會傳到我們的伺服器。刪除 App 就會一起刪除。</p>
""" + zh_ads('獎勵廣告（由你選擇觀看，換取遊戲內獎勵）和插頁廣告') + ZH_PURCHASE + zh_common_tail() + f"""</section>
<section id="en" class="en">
<h2>English</h2>
<p>This policy covers the QiYun Avengers Android app by {DEV} ("we").</p>
<h3>We collect no personal data ourselves</h3>
<p>There is no sign-up or login. Progress and settings are stored only on your device and never sent to our servers. Uninstalling the app deletes them.</p>
""" + en_ads('rewarded ads (which you choose to watch for an in-game reward) and interstitial ads') + EN_PURCHASE + en_common_tail() + "</section>"))

APPS.append(dict(
    slug='taipei-signal-hud', zh='青紅燈', en='TaipeiSignalHUD',
    desc='台北、新北、基隆前方路口燈號抬頭顯示（Android）',
    body=head('青紅燈', 'TaipeiSignalHUD') + f"""<section id="zh">
<p>{DEV}（以下稱「我們」）開發的《青紅燈》Android App，在開車時顯示前方路口的紅綠燈。這份政策說明 App 會處理哪些資料。</p>
<h2>位置</h2>
<p>青紅燈需要你的精確位置（GPS）才能判斷你在哪條路、前方是哪個路口。你開啟抬頭顯示時，App 會在前景服務中持續取得位置，關掉顯示就停止。</p>
<p>為了查詢前方路口的燈號，App 會把目前的座標傳到我們的燈號伺服器。伺服器用它找出附近的路口並回傳燈號；伺服器的紀錄只用來維持服務運作和改善燈號資料，不包含你的姓名、帳號或廣告 ID，也不會提供給其他人。</p>
<h2>其他權限</h2>
<ul>
<li><b>通知</b>：Android 規定前景服務必須顯示通知。</li>
<li><b>顯示在其他 App 上層</b>：讓燈號浮在導航畫面上。</li>
<li><b>網路</b>：查詢燈號、更新路口資料、顯示廣告。</li>
</ul>
<p>青紅燈不需要註冊或登入。設定只存在你的裝置裡。</p>
""" + zh_ads('獎勵廣告：只有在設定頁按「手動更新資料」時播放一則，看完才更新；其他畫面都沒有廣告。') + zh_common_tail('和我們的燈號伺服器') + f"""</section>
<section id="en" class="en">
<h2>English</h2>
<p>TaipeiSignalHUD by {DEV} ("we") shows the traffic lights at the intersections ahead while you drive. This policy explains what data the app handles.</p>
<h3>Location</h3>
<p>The app needs your precise (GPS) location to work out which road you are on and which intersection is ahead. While the heads-up display is on, the app keeps receiving your location in a foreground service; turning the display off stops it.</p>
<p>To look up the signals ahead, the app sends your current coordinates to our signal server, which finds the nearby intersections and returns their signals. The server's logs are used only to keep the service running and improve the signal data; they contain no name, account or advertising ID and are not shared with anyone.</p>
<h3>Other permissions</h3>
<ul>
<li><b>Notifications</b>: Android requires a notification for the foreground service.</li>
<li><b>Display over other apps</b>: shows the signal on top of your navigation app.</li>
<li><b>Internet</b>: signal lookups, intersection data updates and ads.</li>
</ul>
<p>There is no sign-up or login. Settings are stored only on your device.</p>
""" + en_ads('a rewarded ad only when you tap "update data manually" in Settings; the update runs after the ad, and there are no ads anywhere else.') + en_common_tail(' and our signal server') + "</section>"))

# ---------------------------------------------------------------- write
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, 'style.css'), 'w').write(CSS)
open(os.path.join(OUT, '.nojekyll'), 'w').write('')
for a in APPS:
    d = os.path.join(OUT, a['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(page(f"{a['zh']} 隱私權政策 · {a['en']} Privacy Policy", a['body']))
items = '\n'.join(f'<li><a href="{a["slug"]}/">{a["zh"]} {a["en"]}</a><small>{a["desc"]}</small></li>' for a in APPS)
index = f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>隱私權政策 · Privacy Policies</title>
<link rel="stylesheet" href="style.css">
</head>
<body><main>
<h1>隱私權政策</h1>
<p class="meta">{DEV} 的 App 與遊戲 · Privacy policies for apps and games by {DEV}</p>
<ul class="apps">
{items}
</ul>
<footer>聯絡 Contact：<a href="{CONTACT}">idleenginestudio@gmail.com</a> · <a href="../">工作室首頁 Home</a></footer>
</main></body>
</html>
"""
open(os.path.join(OUT, 'index.html'), 'w').write(index)
print('\n'.join(a['slug'] for a in APPS))
