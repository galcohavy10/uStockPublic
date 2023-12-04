note: the publised products are in uStock-V2-AI

[Visit this link to see a product demo of this social media app.](https://github.com/galcohavy10/galcohavy10/assets/96891588/48429396-a5dd-43a7-bd87-ca4903e56129
)

# uStock

# <img width="245" alt="Screen_Shot_2023-03-19_at_8 11 17_PM-removebg-preview" src="assets/logo v1.2/logov1.3IOS copy.jpg">


All-in-one game interface for interactive personal improvement. 

Define goals, access specific interest communities (professional, sports, music), in-app token currency, compete with friends, groups and communities to achieve a higher ranking stock value (dictated by achievement in communities).

## Minimum Viable Product:
Self-Improving game. Fun to compete, create posts and discuss with ppl in your community + use community tools.
Main objective: Increasing one's stock value.

## Key Features

### 1. Ability to generate wealth and status with real value currency* in app.

- Users will not be able to (at least to a significant degree) be valued highly for useless and ultimately fake metrics such as flexing cars they rented on people and making others feel inferior. People will be rewarded for objectively good deeds they do, outputted value in real world and productivity in application community. 

- People can utilize wealth to join more communities, gain status and have access to speak at a "higher volume" in a community. 

- Ultimately, there will be real prizes such as concert tickets and grand pianos for those leading in the sector of piano and surfboards and surf trips for those who are surfing leaders. 
###### A late-game version of this will be compensating all creators to some degree.



### 2. Interaction with communities

- Users are surrounded with people who are also striving for success in your domain and can critique and give insight, fast-tracking success of a user who is trying to improve at any given skill. 
- Users can gain access to new hobbies, start building a portfolio (that will also give them equity in themselves: hence the need for a currency) of skills and achievements in a given community and be a valued member of a community.
- Additionally, most communities will have a built-in personalized tool made with the help of the most competent members in that community. 



### 3. Self-Improvement

- Ultimately, and using the features listed above, users can improve their life. They will be focusing in on the things they care most on their life and improving those things. For example, a triathlon father joins the app and gains higher stock value for his 'dad log' in the dad community as well as his triathlon times.
- Users will be able to use analytical data to see how well they have enacted positive change in the most important "aspects" of their life, hence the reason we user the term "aspect" to describe these communities.
###### This is why the system will be so self propagating and spread the most amount of change in the smallest period of time. Being such a great platform for actual improvement in people's lives, people will naturally 'extract' the app to the next person. Suppose the hypothetical: Person B: "Wow, how'd you lose so much weight these past few months?" User A: "uStock..." (now user) User B: I'm skeptical but I'll try it and see how it goes. | Person C: "How'd you get so good at math this semester?" User B: "uStock...". rinse. repeat.
##### -> All Roads Lead to uStock <-



## Steps to Success:

### 1. Build Product
Create a prototype that is useful enough to retain boarded entities* for extended periods of time.

### 2. Optimize Onboarding and Funnel Experience
Improve the onboarding process and the full funnel experience for long-term users, minimizing acquisition costs.

### 3. Viral Growth
Implement group entity competitions and exclusivity factors to attract and retain users. As growth occurs, the cost of virality reduces due to the increase in the perceived value of the on-platform currency*.

### 4. Word of Mouth (Free Viral Marketing)
Leverage the natural tendency for people to talk about ongoing campaigns. The growing value of the in-app currency will prompt users to seek quick cash, encouraging referrals and enhancing the word of mouth strategy. People like discovering a new tool, so build something so undeniably good it will feel good for someone to tell a friend about.

### 5. Repeat these steps as necessary for sustained success.

## Infrastructure
```
┌───────────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
│                       │◄──────│                       │◄──────│                       │
│   Frontend:           │──────►│   Backend:            │──────►│   Database:           │
│                       │       │   API                 │       │                       │
│   ──────────────────  │       │   ──────────────────  │       │   ──────────────────  │
│   • Java (android)    │       │   • Node.js           │       │   • MongoDB Atlas     │         
│   • SwiftUI           │       │   • Mongoose          │       │   • AWS               │
│   • Web (TBD)         │       │   • JSON/BSON         │       │                       │
│                       │       │   • Express           |       │                       │
│                       │       │                       │       │                       │
└───────────────────────┘       └───────────────────────┘       └───────────────────────┘

```



                                       /|\
                                        |
*ILLUSTRATION OF INFRASTRUCTURE/STACK*  | 
- ###### It is also worth noting that the addition of external APIs makes this a bit more complex, but to keep it simple these are the bare basics of the infrastructure.


## Libraries:
We are currently using standard libraries only (such as express for routing, cors for middleware, openAI and sharp for file compressions).

Staying minimal and secure with added libraries is our target. We want to keep the application from being bloated, costing more server weight and speed.
MOST IMPORTANTLY, we never use libraries that are not being maintained. We are not building a jenga tower that will fall when some random developer stops taking care of our dependencies. Use trusted libraries or build it yourself.


## USAGE:
-I strongly recommend asking GPT-4 about code you don't understand.
Installation Prerequisites Node.js (version 14 or higher) MongoDB (version 4.4 or higher) npm (version 6 or higher) and Xcode for running frontend.
-Run backend inside /uStock-IOS-V2/Backend/api folder for node server with command "node index".
-Run iphone app by clicking the file in uStock-V2-AI called "uStockIOS-V2-AI.xcodeproj"

Authentication necessary for:
-MongoDB using mongodb-atlas to find uStock "test" in Project0. 
-Checkin AWS.
-Checking OpenAI API usage.
*You need to contact Gal for access, these can all be accessed through his cohavygal google account.*
-Additionally, accessing heroku server to make global changes also needs 2-factor auth so contact me directly in emergencies. You may run "heroku logs" in node to try and parse console messages from heroku server.


### Steps
Install Git: Before you can clone a repository, you need to have Git installed on your computer. You can download and install Git from the official website: https://git-scm.com/downloads.

#### Use a terminal
(Command Prompt, PowerShell, or Terminal on macOS/Linux) and navigate to the folder where you want to clone the repository. For example, if you want to clone the repository in the "projects" folder located in your user directory, you can run:

bash (terminal):

"cd ~/projects" Replace ~/projects with the appropriate path on your system.

Clone the repository: In your terminal, run the following command:

bash (terminal):

"git clone https://github.com/galcohavy10/uStock-Development.git" The repository will be cloned into a new folder named "uStock-Development" in the current directory. You can now navigate to the newly created folder:

bash (terminal):

"cd uStock-Development" You have now successfully cloned the "uStock" Git repository from "galcohavy10" on GitHub and can start working on the project!


##### Order of Development:
1. Mobile - IOS then Google Play
2. Web App - In React.js or Angular.js
3. Maintenance and product feature growth.

**The key here is to be focused primarily on the product with marketing being secondary, good products market themselves.**

##### Key Terms
Entities: Groups, communites such as "Surfing" or "Rowing of North Carolina". Users such as "John Grapeseed". 

Boarded Entities: When onboarding new users or groups, ~40% at minimum are not going to remain using the product after initial period approximating a week. Boarded entities are the people who are actually "on-board" and are using the app after the intense initial dropoff period.

Currency: Users can trade stock in others to express interest, try and gain money for their wallet and show support. The wallet can, primarily, gain access to new communities.

Aspects: Aspects are important categories established on the app that are broad. Examples include: Piano, Running, Soccer, Chemistry and Travel. It is important to note that most large entities such as groups or inter-user/inter-group competitions will also be grouped into some broad aspect.
