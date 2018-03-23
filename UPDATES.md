# Sagefy Development Updates

This is a reverse chronological listing of updates on Sagefy's progress. I will try to do these biweekly.

You can sign up for email updates at https://sgef.cc/devupdates

## UPDATE -- 2018 Mar 19

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### 2018 Mar 5 - 2018 Mar 18

* Built example for ["Spectrum and Color"](http://em.sagefy.org/examples/spectrum-and-color)
* Fixed issue where users could not log in or out intermittently. Redis was trying to write to disk; we use Redis only to track sessions and cache. Now we log 500s to help faster debugging.
* Continuing on Medium article on the 8 "big ideas"

### Upcoming Two Weeks: 2018 Mar 19 - 2018 Apr 1

* Build remaining 2 interactive examples for the Intro to Electronic Music: Sound Parameters unit.

### Feedback

Feel free to reply to this address! You can also go to http://sgef.cc/feedback and add feedback or ideas there.

## UPDATE -- 2018 Mar 5

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### 2018 Feb 19 - 2018 Mar 4

* Continuing on Medium article on the 8 "big ideas"
* Built example for "Frequency and Pitch"
* Working on next batch of interactive examples

### Upcoming Two Weeks: 2018 Mar 5 - 2018 Mar 18

* Build remaining 3 interactive examples for the Intro to Electronic Music: Sound Parameters unit.

### Feedback

Feel free to reply to this address! You can also go to http://sgef.cc/feedback and add feedback or ideas there.

## UPDATE -- 2018 Feb 19

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### 2018 Feb 5 - 2018 Feb 18

* Continuing on Medium article on the 8 "big ideas"
* Working on next batch of interactive examples

### Upcoming Two Weeks: 2018 Feb 19 - 2018 Mar 4

* Build remaining 4 interactive examples for the Intro to Electronic Music: Sound Parameters unit.

### Feedback

Feel free to reply to this address! You can also go to https://sgef.cc/feedback and add feedback or ideas there.

## UPDATE -- 2018 Feb 5

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### 2018 Jan 22 - 2018 Feb 4

* Started next Medium article on the 8 "big ideas"
* Working on next batch of interactive examples
* Removed feedback component on site
* Migrated from virtual-dom to snabbdom
* Migrated from Mocha, Chai, & Sinon to Jest
* A few minor bug fixes

### Upcoming Two Weeks: 2018 Feb 5 - 2018 Feb 18

* Build remaining 4 interactive examples for the Intro to Electronic Music: Sound Parameters unit.

### Feedback

Feel free to reply to this address! You can also go to
https://sgef.cc/feedback
and add feedback or ideas there.

## UPDATE -- 2018 Jan 22

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### 2018 Jan 8 - 2018 Jan 21

* Finished interactive example for amplitude/volume (Intro to Electronic Music: Sound Parameters unit).
* Implemented Prettier for the client code.

### Upcoming Two Weeks: 2018 Jan 22 - 2018 Feb 4

* Build remaining 4 interactive examples for the Intro to Electronic Music: Sound Parameters unit.

### Feedback

Feel free to reply to this address! You can also go to
https://sgef.cc/feedback
and add feedback or ideas there.

## UPDATE -- 2017 Jan 8

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### 2017 Dec 11 - 2018 Jan 7

* Happy New Year!
* Switched from flake8 to pylint to support 2 space/indent across the board.

### Upcoming Two Weeks: 2018 Jan 8 - 2018 Jan 21

* Build 5 interactive examples for the Intro to Electronic Music: Sound Parameters unit.

### Feedback

Feel free to reply to this address! You can also go to
https://sgef.cc/feedback
and add feedback or ideas there.

## UPDATE -- 2017 Dec 11

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### 2017 Nov 27 - 2017 Dec 10

* No updates. Tis the season for illness :)

### Upcoming Two Weeks: 2017 Dec 11 - 2017 Dec 24

* Build 5 interactive examples for the Intro to Electronic Music: Sound Parameters unit.
* Build 4 interactive examples for the Intro to Electronic Music: Human Hearing unit.

### Feedback

Feel free to reply to this address! You can also go to
https://sgef.cc/feedback
and add feedback or ideas there.

## UPDATE -- 2017 Nov 27

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### 2017 Nov 13 - 2017 Nov 26

* Created the new "unscored embed" card kind. Simply specify a URL and it will be embedded on the page! The name may seem silly... but there may be a "scored embed" and "peer-scored embed" in the future.

### Upcoming Two Weeks: 2017 Nov 27 - 2017 Dec 10

* Build 5 interactive examples for the Intro to Electronic Music: Sound Parameters unit.
* Build 4 interactive examples for the Intro to Electronic Music: Human Hearing unit.

### Feedback

Feel free to reply to this address! You can also go to
https://sgef.cc/feedback
and add feedback or ideas there.

## UPDATE -- 2017 Nov 13

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### 2017 Oct 30 - 2017 Nov 12

Didn't complete as much as hoped.

* Posted on Product Hunt: https://www.producthunt.com/posts/sagefy/
* Updated transactional email copy to include reply-to-unsubscribe copy.
* Deployed build process and outlined script for Web Audio API examples. Started on Amplitude example.

### Upcoming Two Weeks: 2017 Nov 13 - 2017 Nov 26

* Build 5 interactive examples for the Intro to Electronic Music: Sound Parameters unit.
* Build "embed (view)" card kind (name pending)

### Feedback

Feel free to reply to this address! You can also go to
https://sgef.cc/feedback
and add feedback or ideas there.

## UPDATE -- 2017 Oct 30

Thanks for signing up for the Sagefy development updates newsletter. I will be sending updates biweekly to help track progress on Sagefy.

### Recent Changes

Because this is the first newsletter, I'm including some of the highlights of the past few months. Normally this newsletter will be pretty short.

* Entirely new content creation system, based on usability testing.
* Created a test "suggest" page: suggest new subjects and upvote too. http://sagefy.org/suggest
* Created repeatable process and faster, easier local dev with Docker Compose.
* Some API endpoints have been split for greater flexibility.
* Migrated from RethinkDB back to PostgresQL.
* Updated service test coverage to 96%.
* Building out a full sitemap for Google indexing.
* Font update from Georgia to Rubik. Come check it out!
* Lots of minor copy changes and bug fixes, styling consistency updates and usability improvements.
* Several new posts on Medium. http://stories.sagefy.org/

### 2017 Oct 16 - 2017 Oct 29

**Page Card Kind**: Sagefy always had video cards and choice cards. I've added the ability to create page cards. Page cards are written content. For now, formatting options include bold, italic, headings, and embedding images.

There is a new page card for each of the 29 units in the Electronic Music subject. The content is the same as the video for each unit, just in written form instead of video. Here is an example https://sagefy.org/cards/PC9ac99ZQqWR-ZiEyP0wgw

### Upcoming Two Weeks: 2017 Oct 30 - 2017 Nov 12

Beginning work on interactive examples -- using the Web Audio API -- of each of the 29 Electronic Music units. See the list at https://github.com/heiskr/sagefy-electronic-music

This will also be a new card kind, though I haven't picked a name yet.

### Upcoming major items in the backlog

* Completing interactive examples for Electronic Music subject.
* Updating the state management system for the client code.
* Rebuilding the suggest page based on feedback.
* Enable editing content from the web interface.

...and about 120 more tasks currently.

### Feedback

Feel free to reply to this address! You can also go to
https://sgef.cc/feedback
and add feedback or ideas there.