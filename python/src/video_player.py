"""A video player class."""

from .video_library import VideoLibrary
is_playing = False
previous_video = None
is_paused = False

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        all_vids = self._video_library.get_all_videos()

        unsorted_vids=[]
        sorted_vids = []
        print("Here's a list of all available videos:")

        for vid in all_vids:
            tags = "["

            for tag in vid.tags:
                tags += tag + " "

            tags = tags.strip()
            tags += "]"
            unsorted_vids += [f"{vid.title} ({vid.video_id}) {tags}"]
        sorted_vids = sorted(unsorted_vids)
        for thing in sorted_vids:
            print(thing)

    def play_video(self, video_id):
        global is_playing
        global previous_video
        global now_playing
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        now_playing = self._video_library.get_video((video_id))
        if now_playing == None:
            print("Cannot play video: Video does not exist")
            previous_video = now_playing

        else:
            if is_playing == True:
                if previous_video == None:
                    print(f"Playing video: {now_playing.title}")
                else:
                    print(f"Stopping video: {previous_video}")
                    print(f"Playing video: {now_playing.title}")
                previous_video = now_playing.title
            else:
                print(f"Playing video: {now_playing.title}")
                is_playing = True
                previous_video = now_playing.title


    def stop_video(self):
        global is_playing
        if is_playing == True:
            print(f'Stopping video: {now_playing.title}')
            is_playing=False
        else:
            print("Cannot stop video: No video is currently playing")
        """Stops the current video."""



    def play_random_video(self):
        """Plays a random video from the video library."""



    def pause_video(self):
        global is_paused
        global now_playing
        if is_paused == False:
            is_paused = True
            print(f"Pausing video: {now_playing.title}")
        else:
            print(f'Video already paused: {now_playing.title}')

        """Pauses the current video."""



    def continue_video(self):
        """Resumes playing the current video."""
        global is_paused
        global now_playing
        if is_paused == True:
            print(f"Continuing video: {now_playing.title}")



    def show_playing(self):
        global now_playing
        output = f"Currently playing: {now_playing.title} ({now_playing.video_id})"
        tags = "["
        for tag in now_playing.tags:
            tags += tag + " "
        tags = tags.strip()
        tags += "]"
        output += " " + tags
        print(output)

        """Displays video currently playing."""



    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """


    def show_all_playlists(self):
        """Display all playlists."""



    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
