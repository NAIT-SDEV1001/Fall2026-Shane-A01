class VideoGame:
    def __init__ (self,title: str, platform: str, hours_played: int)-> None:
        self.title = title
        self.platform = platform
        self.hours_played = hours_played
    
    def add_play_time(self, hours: int)->None:
        self.hours_played += hours

    def has_been_played(self)->bool:
        return self.hours_played > 0

    def __str__(self)->str:
        return f"{self.title} on {self.platform} ({self.hours_played} hours played)"

    def __repr__(self)-> str:
        #!r will place quotes around the string
        return f"VideoGame({self.title!r},{self.platform!r},{self.hours_played})"

def main():    
    
    games: list[VideoGame] = []#optional type hint. A list of VideoGame Objects

    while True:
        title = input("Game title (q to finish): ")
        if title == "q":
            break

        platform = input("Platform: ")
        hours_played = int(input("Hours played: "))       
        game = VideoGame(title, platform, hours_played)
        games.append(game)
        #OR
        #games.append(VideoGame(title, platform, hours_played))

    
    for game in games:
        print(game)

    print("\nGame titles")
    for game in games:
        print(game.title)  
    
if __name__ == "__main__":
    main()
    