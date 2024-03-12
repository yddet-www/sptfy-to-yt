<h1>sptfy-to-yt</h1>

<p>
Welcome to my project! This is a simple Spotify to YouTube playlist converter built in Python as a console application that makes use of Spotify's web API and YouTube data API. I made this just as a side project for no particular reason other than to have options on which music platform I want to use. But since I've been using Spotify for a while now, my playlists have bloated in size and making a separate playlist on YouTube and searching the songs then adding them to it one by one can be a pain in the neck. And I know I could've used an existing app that does this and more, but where's the fun in that? Anyway, I'll walk you through how this console app works and the details of the code.
</p>

<h1>How it works</h2>

<h2>Overview</h2>

<p>
Before jumping into the details of the code, I will go over the general process of this app. This application makes use of a text file to store and recall previous sessions, where the first line of the text file will always hold the data for how much of the user's quota is left and the date for their quota reset. I implemented a quota system as a way to work around YouTube's quota limit, and the quota of a user decreases for each time a track from a playlist is processed. This will be the first process of the app and once their quota amount is set, the application will proceed to the menu screen. The menu provides the user with 7 options. There are two basic processes that returns the date for the user's next reset date, and their remaining quota. They are also provided the option to add an entry to a queue. An entry is a "Playlist" object consisting of the ID of its source (Spotify) playlist, the ID of its target (YouTube) playlist, and a list of tracks retrieved from its soruce. All these data can be retrieved by the user, as there is an option to check whichever entry of the queue they wish for. Finally, they can process an entry from the queue to begin the transfer, limited to 50 songs until the next reset date. The reset date occurs every 02:00 AM CST, where user's quota limit will be brought back to 50. When the user exits the application, the current session is saved by writing to the text file. The first line (holding the quota data) will be rewritten with the amount of quota left after their most recent session along with the next reset date. Every entry in the queue that have yet to be completely processed will also be saved; each line after the first representing a single entry in the format [source;target;track(1); ... ;track(n)].
</p>

<h2>Playlist class</h2>

<p>
This is a simple class module, holding the following variables
  <ul>
    <li>
      source: ID of Spotify playlist
    </li>
    <li>
      target: ID of YouTube playlist
    </li>
    <li>
      tracks: list of music tracks
    </li>
  </ul>
</p>

<h2>Spotify API module</h2>

<p>
  
</p>

<h2>YouTube API module</h2>
