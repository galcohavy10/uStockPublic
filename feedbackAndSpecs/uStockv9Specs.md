DUE OCT 1st: uStock v9

SUMMARY: along with beauty and better design and crusihing the shit out of bugs, this update will most importantly add WORKFLOWS and suggestions for AI. And the use of Health to track live what other users are getting in competitions, provide better task suggestions, community exp. Etc.

FIXES (ALL)
- [x] You, instead of profile
- [x] Close uHero customization on sending a message
- [x] fix overloading task suggestions 
- [x] fix sizing on homepage icons, and fix their color as well: see where else this is possible (like post community icons)
- [x] Fix the sheer amount of colors and overuse of them simplify to a customized palette
- [x] BUG: notifications not clicking first try
- [x] INSTANT loading on everything simple like upvotes and such on frontend
- [x] BIG BUG: fix un clickable competitions in following feed view 
- [x] BUG: user explorer scrolling weird once you expand. Consider making its Frame even smaller and fix all nested scrollview issues.
competitions, etc. Intuitively, like editing a google doc
- [x] Simplify interface, remove browsing competitions for new users on homepage or even for users who have competitions. Also, move investedUserStocks to compete tab for now, where the leaderboard will always show.
- [x] Instant loading cache empty things (cache an empty post and competitions so loading page looks more full. then underneath some: "loading..." Failed if it fails. Upvotes, downvotes, tasks, OMIT bc this sorta exists already. NEED user to cache friends posts, stock, etc in a diff update
- [x] Question mark on stock should be maybe near the stock number 
- [x] Logo’s ugly, should match new chosen colors and shades.
- [x] Health page doesn’t create post
- [x] fix persistent media load on different chats
- [x] Scroll to videos, photo or gif after flicking it on in chat
- [x] Request new community feature 
- [x] I can’t buy or sell stock errors unclear: better messaging there
- [x] Audio-chat feature should work with ringer off and should be called voiceover. Maybe use different icon
- [x] Make sure to reverse the order of competitions where they’re listed in the wrong order in taskcreation postcreation 
- [x] Fix notification text alignment
- [x] Make it so that the scroll bar doesn’t just go to a random number but goes to the amount of stock that I have left to SELL. Also, make sure uppermax changes proportion of slider.
This also made the disabling of buttons unnecessary and the view overall more intuitive
- [x] For tasks suggestions on randomizing old make sure that the world is a natural language word not a placeholder like “a” or space char
- [OMIT] Things been hardcoded too many times? Add extensions on objects for tedious tasks or a global var if necessary: I cannot think of an example lol.
- [x] BUG: first updateProgress() on competition progress bar not working
- [x] XYZ POSTED TO UR COMPETITION notification, send notifs on post adds!
- [x] Fixed user parsing on first time submitting a text post
- [x] More author pics, more quotes on same authors
- [OMIT] We need the actual site to do universal links.
- [OMIT] Stop-generating stops Server Event for OpenAI: not offered, can figure out later. Doesn't bother user
- [OMIT] Image cropping doesn’t let me go down or up: We will do this kinda stuff with new gen images
- [x] fix ugly and buggy menu of an aspectview
- [x] Detailed Comp View knows if userIsMember() and display accordingly.
- [x] Wrong username (galcohavy10) and no pfp on my new comp: What is this issue? Fix.
- [x] fix overaggressive watch button covering whole icon
- [OMIT] When you click icons they should take you to parent of the tab: using render ID: meeds a custom tab bar.
- [x] fix create post with tasks bug: not showing anything
- [OMIT] Make sure shared post opens even if a sheet is open at the time using a fullscreencover : can't exactly see issue here.
- [OMIT] This was posted to a competition on comp posts: unimportant.
- [x] The customizing of AI is non-intuitive (like for clicking the uHero instead maybe and should definitely open a fullscreen popover)
- [x] simplified loading spinner instead to minimize user confusion it follows standard. HUMAN INTERFACE!
- [x] More tutorials for things like tradestockview to tell user this is just a way to chip in some support for a friend.
- [x] Delete competition 
- [x] fixed watch button bug and loading of stocks looked bad
- [x] Fixed empty browse comps view bug
- [x] make + button on comps nice
- [x] make post view menu intuitive
- [x] fixed the incessant watch button bug, one condition was still showing the button across whole thumbnail
- [x] ringer not on, still can play VoiceOver in uHero


BUILDS (25)
- [x] Add default tasks for new users, such as create bio, follow someone etc. DO THROUGH BACKEND
- [OMIT] Immediately learning by doing on the initial tutorial, tapping sample things like fake task suggestions, etc. This concept intuituvely carries over to actual tutorial : there's a lot of learning by doing already and this discourages development of a friendly UI (shorter tutorial == simpler + better app)
- [x] Comp status, CLOSED, Who won on frontend, etc.



	
- [ ] periodic competition updates for currencies with sync available
- [ ] health popup for certain communities
- [ ] health helps with task suggestions a bit


- [ ] Denying or accepting a task suggestion should affect every next suggestion (unless you’re denying a duplicate)
- [ ] Editpost fullstack
- [ ] Messages from the editor I can send only for things like: Since you’ve been gone: what the app development has fixed, etc... when u open the app
- [ ] Potentially change the leaderboard to look more like a bell curve or leagues. And GAMIFY, so different skins and levels for different things you do (as well as badges).

- [ ] modify system messages and chantajes to suit workflow and make sense with bees boo 
- [ ] WORKFLOWS built in backend and have the ability to generate them
- [ ] Workflow interface and explore built in like suggested questions

- [ ] Build mechanism to move user from tab to tab to do things like when posting, take user to home page and minimize the “waiting time” by not making the user see the waiting circle
- [ ] Create in-app artificial popover notifications to show the user things are happening like the loading bar for a post loading while the user is scrolling through home
- [ ] Stocks are more thorough, so they can show stats through stock, like chats sent, tasks created finished, on-task percentage, posts created, etc... 
- [ ] Using stock detailed history: Make analytics available intuitively and beautifully.
- [ ] Save AI Preferences to Phone more efficiently, this is only necessary for simple bools like showDefaultPrompts: USE CACHE WITH OBSERVABLE OBJECT not userpreferences
- [ ] Add more reload buttons (tasks, maybe competitions, profiles, posts) & maybe use scrolling up to do this
- [ ] Confirmation codes on phones and emails, and a FORGOT MY PASSWORD
- [ ]  Default responses to some questions on uHero (“Learn” tab resources programmed in and a bit random): basically has best resources for communities (yousician for music, myfitnesspal and good subreddits and books, etc…). 
- [ ] Add better App Store pics and graphics that fit primary colors and new logo. 
- [ ] AI can create tasks through chat
- [ ] Share my entire AI chat to a post
- [ ] MORE USE OF MONEY, creating competitions as wagers and show the wager that's going on. Can be uBux (ice baths, etc) needs to be accepted by all parties
- [ ] Detailed task view
- [ ] Stock & wallet act more as one as BUX: abstract away buying your own stock and just automatically add value to people's wallets. MAKE THIS CONCEPT MORE INTUTIVE
- [ ] Beesboo makes sense from the beginning tutorial and change the name of the AIs. He's the character guiding through your app and he's doing all the AI suggestions as well. 
- [ ] Make media type’s location locked in post creation
- [ ] Get a challenge for a competition from the founder immediately
- [ ] Badge awards for hitting goals like 100 tasks, etc. but mostly the amount of XP you have in a community can make you any level from 1-100 (beginner to master)
- [ ] Notifications from BeesBoo sometimes!
- [ ] some user lists primitive should be clickable and also have their profile pics there
- [ ] Make the prompt for each bot more concise as well as powerful: how can they be tailored for diff use cases of workflows? Do this for EVERY bot.
- [ ] Embedding past conversations into AI
- [ ] Health API or API data posts (basically organized text)
- [ ] The teaser views should have info icons
- [ ] Instruction recommendations (teach me Spanish and grade responses, quiz me on vocabulary with sentence usage)
- [ ] Save a workflow with AI: ask this on a message with a new workflow. Can select these defaults in customization as well
- [ ] Show watchingCompetition posts on the following feed as integrated
- [ ] Use separate files for video thumbnails full-stack and cache them aggressively 

BEFORE SUBMISSION:
- [ ] Change tutorial to more bees boo and simplify whatever possible






















