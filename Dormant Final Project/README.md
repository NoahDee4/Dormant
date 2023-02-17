# How to run on your computer
Download all the files and add them to your IDE (Coding Environment). Open the terminal (assuming you are on CS50's IDE, you should already have flask installed). Then, simply cd Dormant and then run flask run. You should see a URL in your terminal. Press it. 

# Youtube Video:
https://youtu.be/L__tZ3-srg8

# Welcome to Dormant at Yale. . . 🛌
Hi there! My name is Noah Dee, a first year student at Yale University. My app/website is titled Dormant at Yale, which essentially helps you find roommates based on your preferences. Essentially, what the app does is that it takes your preferences and returns people who have similar interests, lifestyles, and living habits as you do. The goal of this app is to help you find people you want to room with in your subsequent years at Yale, and also making sure that you end up getting along together. The main reason why this website is so useful is due to the fact that it is in real time and takes real user inputs. In essence, all the students who could be your potential roommates are actually Yale students who might need roommates one day! Put shortly, Yalies can actually use this! I know I’ll certainly use it in case I can’t find roommates for next year.

## Getting Started. . . 🏁
When you first open the application (you can run flask run in your terminal), you will be prompted with the homepage, displaying an image of a room and some text of the app's main goal: to find you a roommate match based on preferences, interests, etc. Above, in the navigation bar, you will see two options: **Register for an Account** and **Logging in**.

### Registering for an account
To register for an account, you will need three main components:
* Your Full Name
* Your Email
* Your Password

Why does **Dormant** look for these three specific components? Well, first off, it would be ideal for your roommate match to know your full name that way they can reach out to you. The same logic applies for your email. If you had further questions about their living habits, you can reach out to them via the chat tab or you can email them directly to get to know them better. As with all websites that are account-based, you will need a secure password to ensure you can safely log in and out of your account. To ensure that your password is strong enough, the website will not allow you to crete an account unless your password is at least 6 characters and includes at least one special character. If successful, you will be directed to the **Login page**.

### Logging In
The log in page has two main purposes: if you recently created an account, you can simply re-enter all of your information and log into the website. However, if you are a returning user, you can simply press the log in button and enter your credentials. If you try to enter a username that does not exist yet, you will be directed back to the register for an account page, where you'll need to make an account, and then may proceed to log in. Assuming your credentials are correct, you will be directing to the main **Manual Page**.

## Manual Page. . . 📚
The manual page gives users a basic sense of the app, how to navigate the app, and what they should gain from the app. Essentially summarized, users can expect names and emails of potential roommates based on their preferences. It also gives a detailed list of instructions of how they should proceed:
* 1. Fill out the preferences form
* 2. Get matched
* 3. Use the chat feature
* 4. View their profile
* 5. Update profile (if needed) and get rematched.

Each of the pages will be explained below. . .

## Filling out the Preference Form. . . ☑️
This form should be the first thing you do after reading the instructions from the manual. Essentially what this page consists of is a series of 10 questions that take your preferences into account. Questions range from anything from "How does your typical weekday look like?" to "What's your music taste like?". The idea behind this page is to collect your individual preferences, load them into a database and match you with somebody of similar preferences. Don't worry about getting every single detail down to the technicality, you can always **Update your preferences** later! And once you do update your page (explained later), you can find new roommates based on such preferences!

## Getting Matched. . . ➡️
After filling out the preferences form, you will automatically land on the Getting Matched Page. Based on your preferences from the form, you will see different people. For instance, if you selected that you wake up at 8:00am, you will see the name and email of another Yale student who wakes up at a similar time. However, you might see a different name for questions like "What's your cleaning schedule" as you might have a different cleaning schedule that someone else. Ideally, you should see the names of students under each individual category. At the very bottom of the page, you'll see a final header titled "Overall Match". The person who appeared most frequently on your matches, say a student wakes up, sleeps, cleans, etc at the exact same time as you will be considered your overall final match. In otherwords, the person you matched with the most in your 10 metrics will be your overall/ideal match. Their name and email is provided so you can always continue from there, or, you can continue with the **Chat Feature**.

## Chat. . . 🗣️
Need more information about your roommate? Have follow up questions? Worry not, the Chat feature has been implemented to Dormant in order to help you learn more about your roommate and get to know one another. Of course, you can go about emailing them from their listed email, but in case you ever wanted to chat with them through the website instead of email, feel free to send them an email over on this page.

## Profile. . . 👤
The profile page will allow you to see your current preferences based on what you have entered most lately. This proves useful as it is a tracker to see your current ideal roommate.

## Update Profile. . . 🆕
Say WHAT? You no longer like loud pop music? Are you suddenly a fan of Lo-Fi music after that one friend introduced you to "Chill study beats"? Or did you accidentally enter the wrong time for when you wake up? Don't worry, the update feature will allow you to change your preferences based on your new preferences. Note that if you only want to change one of your preferences (ie music tastes), you can opt to keep everything else the same by simply entering what you previously entered. **If you do update your preferences, you can go back to the Getting Matched page and you can see new roommates based on the changes**

## Log out . . . 👋
Done for today? Log out by hitting the log out button. All of your information is saved on a database, so you never have to worry about losing data, or having to re-enter your preferences. We'll catch you later!