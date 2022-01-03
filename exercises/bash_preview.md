## Bash preview

The desire to automate repetitive tasks is a key motivator for the adoption of code in newsrooms. 

Below is a short walk-through intended to demonstrate the power of automation, and often how little code is required to execute useful tasks.

As with most tasks involving code, there are many potential ways to solve a given problem. Here, we introduce the Bash shell and a few basic Unix tools by way of dipping our toes into the world of automation.

> We'll skip the backstory on these tools for now, but never fear, we'll learn more about these tools early in the quarter. Just follow along for now.

Open a terminal shell (on Mac, search for `Terminal`).

On the shell, navigate to your Desktop.

```bash
cd ~/Desktop
```

Download the [Stanford events home page](https://events.stanford.edu/) using either `curl` or `wget` (Mac and Linux machines typically include at least one of these tools by default).

```bash

curl -o events.stanford.html https://events.stanford.edu/

# OR if curl is not available on your machine, try wget:

wget -O events.stanford.html https://events.stanford.edu/
```

You've just downloaded the HTML for the Stanford events home page.

You can view the contents of this file using a code editor, a web browser, or
even common Unix tools such as `cat` or `less`.

> Later this quarter we'll learn more about dissecting and extracting
> data from web pages.

Let's say we wanted to extract the titles of all recent events from
this page and place them in a text file for easier review.


You can use the Unix `grep` utility to find lines in a file that contain
certain bits of text (or even text patterns!).

In this case, let's search for all `h3` tags, which appear to be used to enclose, or "mark up", event titles in the HTML.

```bash
grep h3 events.stanford.html
```

The above should have printed out the event titles wrapped in `<h3>...</h3>` HTML tags to your shell.

If that worked, great! Now let's redirect that output to a text file.

```bash
grep h3 events.stanford.html > events.stanford.txt
```

You can open up this file using a code editor or view its contents
 using `cat` or `less` on the command line.

> Hit `q` to exit out of `less`

```bash
less events.stanford.txt
```

Finally, let's say you wanted to update your text file every day at a certain time. You could place the commands we've used so far into a **shell script**, and then run that script at a set time
each day using a Unix utility known as `cron`.

Create a text file called `events_updater.sh` with the following:

```bash
cd ~/Desktop
touch events_updater.sh
```

Add the following code to the file:

```bash
cd ~/Desktop
curl -o events.stanford.html https://events.stanford.edu/
grep h3 events.stanford.html > events.stanford.txt
```

Next, you can use the built-in cron utility on Linux or Mac to
schedule the script.

> On Macs, you may need to [grant cron permissions](https://www.bollyinside.com/articles/fix-cron-permission-issues-on-macos-catalina-mojave/) to access your file system.

Open the crontab file from the command line using `crontab -e`. This
will open the so-called `crontab` file in the shell's default text editor
(typically Pico or nano by default).

Copy the following into the `crontab` file. Then save and quit.

```bash
* * * * * /bin/sh $HOME/Desktop/events_updater.sh > /tmp/events.stanford.log 2>&1
```

The above schedules the script to run every minute.

After the script runs, you should see the `events.stanford.html` and
`events.stanford.txt` files on your Desktop. If something went wrong,
you can check `/tmp/events.stanford.log` for logs about potential
errors (we configured our cronjob command to pipe errors and other
script outputs to this temporary log file).

That's just a small taste of how we can begin automating useful but repetitive tasks. Of course, there's much room for improvement of this
script, depending on your needs.

What are some improvements you could imagine making?

- Get the dates of events
- Generate a properly structured CSV for use in Excel
- Scrape older events
- Send an email alert when new events crop up
