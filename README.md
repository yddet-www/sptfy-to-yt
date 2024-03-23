<section>
<h1>sptfy-to-yt</h1>

<p>
  Welcome to my project! This is a simple Spotify to YouTube playlist converter built in Python as a console application that makes use of Spotify's web API and YouTube data API. I made this just as a side project for no particular reason other than to have options on which music platform I want to use. But since I've been using Spotify for a while now, my playlists have bloated in size and making a separate playlist on YouTube and searching the songs then adding them to it one by one can be a pain in the neck. And I know I could've used an existing app that does this and more, but where's the fun in that? Anyway, I'll walk you through how this console app works and the details of the code.
</p>
</section>

<section>
  <h1>How it works</h2>

  <h2>Overview</h2>

  <p>
    Before jumping into the details of the code, I will go over the general process of this app. This application makes use of a text file to store and recall previous sessions, where the first line of the text file will always hold the data for how much of the user's quota is left and the date for their quota reset. I implemented a quota system as a way to work around YouTube's quota limit, and the quota of a user decreases for each time a track from a playlist is processed. This will be the first process of the app and once their quota amount is set, the application will proceed to the menu screen. 
    <br> 
    The menu provides the user with 7 options. There are two basic processes that returns the date for the user's next reset date, and their remaining quota. They are also provided the option to add an entry to a queue. An entry is a "Playlist" object consisting of the ID of its source (Spotify) playlist, the ID of its target (YouTube) playlist, and a list of tracks retrieved from its soruce. All these data can be retrieved by the user, as there is an option to check whichever entry of the queue they wish for. Finally, they can process an entry from the queue to begin the transfer, limited to 50 songs until the next reset date. The reset date occurs every 02:00 AM CST, where user's quota limit will be brought back to 50. 
    When the user exits the application, the current session is saved by writing to the text file. The first line (holding the quota data) will be rewritten with the amount of quota left after their most recent session along with the next reset date. Every entry in the queue that have yet to be completely processed will also be saved; each line after the first representing a single entry in the format [source;target;track(1); ... ;track(n)]. On the next session, quota data will be processed along with any saved entries from previous sessions.
  </p>

  <h2>Playlist class</h2>

  <p>
    This is a simple class module, holding the following variables
    <ul>
      <li>source: ID of Spotify playlist</li>
      <li>target: ID of YouTube playlist</li>
      <li>tracks: list of music tracks</li>
    </ul>
  </p>

  <h2>Spotify API module</h2>

  <p>
    The module takes the client ID and client secret values from an environment file that I have omitted (for obvious reasons). If you would like to make use of this app or module, be sure to create your own Spotify API and use your own client ID and secret values.
  </p>

  <ul>
    <li>
      <h3>getToken()</h3>
      <p>
        This method returns the access token for the Spotify API, which will be used for other methods in this module.
      </p>
    </li>
        <li>
      <h3>get_playlist_ID(url)</h3>
      <p>
        This method takes a valid URL of a public Spotify playlist and returns its ID
      </p>
    </li>
        <li>
      <h3>get_playlist(playlist_id)</h3>
      <p>
        Given a playlist ID as an argument, perform an API call that returns a list of dictionaries of all tracks and its respective artists as keys from the given playlist. In a single call, the response is limited to 100 tracks. However, the response will provide a value in "next" that helps to select the next 100 (if any) for that given playlist.
      </p>
    </li>
  </ul>

  <h2>YouTube API module</h2>
    
  <p>
    The module takes the API key from an environment file that I have omitted (again, for obvious reasons). If you would like to make use of this app or module, be sure to create your own YouTube API and use your own API key.
  </p>

  <ul>
    <li>
      <h3>yt_set_credentials()</h3>
      <p>
        Gets the OAuth credentials, which is necessary for our method calls in this module. This will prompt the standard Google authentication page.
      </p>
    </li>
    <li>
      <h3>create_playlist(playlist_title="Made by yddet")</h3>
      <p>
        Taking a string as an argument (defaults to credit me), creates a public empty playlist in the user's YouTube account with the argument as its name and returns the newly created playlist's ID.
      </p>
    </li>
    <li>
      <h3>search_video(keyword)</h3>
      <p>
        Taking a keyword in the form of a string, perform a YouTube search and return the video ID of the first result.
      </p>
    </li>
    <li>
      <h3>insert_vid_to_playlist(playlist_id, video_id)</h3>
      <p>
        Taking the ID of a playlist and video as its arguments, insert the video into that playlist. I've implemented exception handling for the case when a "SERVICE_UNAVAILABLE" exception occurs. The exception will pause the process momentarily before retrying until a maximum number of tries elapses, before finally raising an error.
      </p>
    </li>
  </ul>

</section>
