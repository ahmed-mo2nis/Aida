# Aida - A Privacy Respecting VA

Aida Is An Open Source Privacy Respecting Virtual Assistant For GNU/Linux Systems. Written In Python.

## Features

Aida Is A VA (Virtual Assistant), So It Can Answer Simple Questions Such As : "who are you", "how do i look", "how am i", "where were you born", "how are you". It Can Tell Jokes. It Can Tell Time, Grab Information from Wikipedia. Aida VA Can Also Tell You The Latest Headlines Whether The News Were Political, Financial, Sports. It Can Search The Web For You (Using Startpage Search Engine). Aida Can Tell You The Weather, Open Firefox Web Browser For You. It Can Take Notes Or Even Play Music For You. You Can Turn It Into A Chatbot by Saying "text mode" And You Can Switch Back To Using Voice Commands By Typing "voice mode". You Can use Aida VA to Turn Off/Restart Your Computer. It's In Continuous Listening Mode And Works From The Terminal So Anytime You Want It To Stop Just Say "sleep". For A Full List Of The Voice Commands See the instructions.txt File.

Aida VA Is A Fork Built Upon Both [Melissa](https://github.com/Melissa-AI) And [Jasper Project](https://github.com/jasperproject) So Thanks To The Makers Of These Projects. Aida Is Aimed To Be Simple To Use And Edit. More Modifications And Features Will Be Added Soon.

Aida VA Is Like Siri, Alexa, Google Assistant And Cortana. Only That It Works Offline And Doesn't Track You Or Collect Any Information About You. Watch The Following Videos For More On The Subject Of VAs And Privacy:

[Alexa Video 1](https://www.youtube.com/watch?v=tBd7LTmWaqU) - 
[Alexa Video 2](https://www.youtube.com/watch?v=pnD6vFaWp2k) - 
[Alexa & Siri Video](https://www.youtube.com/watch?v=ZfxA4NpwVBw)

Or Read These Articles :

[Alexa Article 1](https://thenextweb.com/artificial-intelligence/2018/05/24/amazon-cant-explain-why-alexa-recorded-and-shared-a-private-conversation/) - 
[Alexa Article 2](https://www.nytimes.com/2018/05/25/business/amazon-alexa-conversation-shared-echo.html?smid=tw-nytimes&smtyp=cur) - 
[Alexa Article 3](https://boingboing.net/2018/08/12/alexa-bob-carol.html) - 
[Alexa Article 4](https://www.wired.com/story/hackers-turn-amazon-echo-into-spy-bug/)

## How It Works

After You Run It From The Terminal (See Usage Section Below). Aida Will Display A Message Saying "I'm Listening" And All You Have To Do Is Speak With Your Desired Command Or Question. If It Didn't Understand It Will Display A Message Saying "Aida Couldn't Understand Audio" Followed By Another "I'm Listening". If It Does Understand It Will Perform The Required Task After Displaying A Message On The Terminal "Aida Thinks You Said:.....". After It Finishes A Task It Will Keep Posting "I'm Listening" Waiting To Hear The Next Command. If Aida VA Doesn't Hear Anything For A While It Will Keep printing "Aida Couldn't Understand Audio" Followed By "I'm Listening" Until You Ask It To Do A Task For You Or Turn It Off By Saying "sleep" Or Turning Your PC Off Altogether.

When You Speak To Aida VA, A .wav File Is Created Recording Your Voice Command. That File Is Then Passed To The [DeepSpeech](https://github.com/mozilla/DeepSpeech/) Pre-Trained Language Model That Is Already Downloaded To Your PC (See Requirements And Installation Sections) Which Will Recognize Your Voice In The .wav File And Write It To A Text File (.txt) Which Then Will Be Analyzed By Aida VA To Find The Appropriate Response And/Or Task. This Process Usually Takes About A Few Seconds And It Gets Faster After The First Time Usage. For Complete Security And Privacy Of Your Data The .wav File Is Deleted And The .txt File Contents Are Erased Instantly After Each Voice Command Process So You Can Be Sure No Human Or Machine Is Collecting Your Data.

## Requirements

For Now It Only Works On GNU/Linux Systems. I Have Tested It On Debian, Ubuntu And Raspbian. I Haven't Tested It On Fedora Yet But Feel Free To Do That (You'll Have To Install Dependencies Yourself Though Since I Haven't Created A Setup File For Fedora Yet. More On That Later).

In Order To Use The Aida VA To Play Music/Audio Files For You, Your Music/Audio Files Need To Be In The Music Folder In Your Home Directory And (For Some Wierd Unknown Reason!) Your Music Files Shouldn't Be In CAPS Or Contain An Apostrophe !

You Need About 7 GB Of Free Space Since You'll Need To Download The [DeepSpeech](https://github.com/mozilla/DeepSpeech/) Pre-Trained Language Model.

As For Hardware Requirements You'll Need A Microphone. I Used [Kinobo USB Mini Microphone](https://www.amazon.com/Kinobo-Microphone-Desktop-Recognition-Software/dp/B00IR8R7WQ) And It Worked Fine. Whatever Microphone You Intend To Use With Your PC Make Sure To Test It First Using [This Link](https://www.onlinemictest.com/).


## Installation

Open Terminal From Your Home Directory (Either From GUI Or By Pressing Alt+Ctrl+T On Your Keyboard)

Write The Following And Enter Your Password And/Or 'y' When Asked To. Feel Free To Skip Any Of These Commands If You Have One/Some Of Them Installed Already:

```bash
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install git
sudo apt-get install libasound-dev
wget portaudio.com/archives/pa_stable_v190600_20161030.tgz
tar -zxvf pa_stable_v190600_20161030.tgz
cd portaudio
./configure && make
sudo make install
sudo pip3 install pyaudio
```

Close The Terminal Window And Open It Again (Or Move To The Home Directory Using The Command Line) And Type The Following:

```bash
git clone https://github.com/ahmed-mo2nis/Aida.git
cd Aida
chmod u+x setup.py
./setup.py
```
This Last Command Is Going To Execute The setup.py File Which Will Install The Rest Of The Dependencies, Including The [DeepSpeech](https://github.com/mozilla/DeepSpeech/) Pre-Trained Language Model Which Is About 2 GB In Size And Even Bigger When Extracted So You'll Need A Stable, Fast Internet Connection And Some Time Until Everything Is Installed, Enter Your Password To The Terminal Or Type 'y' When Asked To To Complete The Installation Process.

## Usage

After The Installation Is Complete, Close The Terminal Window. Now All You Need To Do To Run Aida VA Every Time You Open Your PC Is By Opening The Terminal From Your Home Directory (Either From GUI Or By Pressing Alt+Ctrl+T On Your Keyboard)  And Typing The Following: 

```
cd Aida
chmod u+x main.py
./main.py
```
And That's It! It Will Keep Running As Explained In The How It Works Section (See Above) Until You Ask To It To Stop (i.e. sleep).

## Note On Voice Recognition Accuracy

In Case You Have Tried Some Of The Features Described Above And Aida VA Didn't Seem To Understand Your Audio That's Probably A Voice Recognition Accuracy Problem. Here Is The Thing : For Offline Voice Recognition Accuracy The Choices Are Very Very Very Limited. I Only Had 2 Choices That Actually Worked Without Problems: [CMU Pocket Sphinx](https://cmusphinx.github.io/wiki/download/) And [DeepSpeech](https://github.com/mozilla/DeepSpeech/). I Like The First One Very Much And I Have The Utmost Respect For Those Who Worked On It But The Problem Is It's Accuracy Is Just Very Poor! And For Some Reason All The Methods Explained Online On How To Improve Its Accuracy  Failed With Me. If You're A Developer And Want To Use CMU Pocket Sphinx Instead Of DeepSpeech Because It's Light Size Then All You Have To Do Is Remove The Lines Installing DeepSpeech From The setup.py File Before Executing It Since I've Already Included Installing Pocket Sphinx In The setup.py File. You Will Also Need To Edit The main.py File In The Aida Directory By Commenting The DeepSpeech Parts And Un-commenting The Pocket Sphinx Parts. It's Basically Done For You As I Explained In The Comments In main.py File Everything You Need To Do To Make It Up And Running Using Pocket Sphinx Instead Of Deep Speech. Aside From Accuracy, Another Reason That Made Me Choose DeepSpeech Instead Of CMU Pocket Sphinx Is The Fact That -Unlike CMU Sphinx- DeepSpeech Community Are Actively Developing Their Project Which Means That It's Accuracy Is Going To Improve Further.

I Know How Painful Voice Recognition Accuracy Apps Since English Isn't My Native Language. You Can Use A File That I've Included To Test How Accurately DeepSpeech Understands Your Voice. This File Basically Repeats What You Say To It (Like A Parrot). To Use It Open Your Terminal From Your Home Directory And Type The Following:

```
cd Aida
chmod u+x parrot.py
./parrot.py
```

## To Do List
- Test Aida VA On Fedora OS (Very Soon)
- Use Aida VA For Home Automation (Soon)
- Make Aida VA Run Programs And Read Articles (Soon)
- Link vision.py With Aida VA Without Breaching User's Privacy (Soon)
- Make Aida VA Check E-mail Without Breaching User's Privacy (Soon)
- Improve Accuracy For Voice Recognition (Not So Soon!)
- Add Aida VA Understand Other Languages (Not So Soon At All!)

## Contributing
Since I Have A Challenging To Do List I Could Certainly Use Some Help! Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. In Case Anything Doesn't Work Even Though You Have Followed The Installation And Usage Instructions Properly Please Let Me Know So That I Can Fix It As Soon As Possible. If You Want To Make A Fork Of Your Own That's Great Too. If You Want To Send Me Your Voice Recognition Accuracy Results After You've Tested The Software That Would Be Super Helpful! Please Make Sure To Update Tests As Appropriate. You Can Always Contact Me Here Or E-mail Me: ahmed_mo2nis[at]protonmail[dot]com

## License
As Explained In The Features Section (See Above) This Is A Fork From Both [Melissa](https://github.com/Melissa-AI) And [Jasper Project](https://github.com/jasperproject). Both These Projects Use The
[MIT](https://choosealicense.com/licenses/mit/) License And The Same License Applies To This Project So Far.
