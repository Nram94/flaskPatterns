from flask import Flask, jsonify

app = Flask(__name__)

# Complex subsystem classes
class MovieLibrary:
    def find_movie(self, title):
        return f"Found movie: {title}"

class StreamingService:
    def stream(self, title):
        return f"Streaming: {title}"

class SubtitleService:
    def enable_subtitles(self, title, language):
        return f"Subtitles enabled for {title} in {language}"

# Facade that simplifies the interaction
class MovieFacade:
    def __init__(self):
        self.library = MovieLibrary()
        self.streaming = StreamingService()
        self.subtitles = SubtitleService()

    def watch_movie(self, title, language="English"):
        movie = self.library.find_movie(title)
        streaming = self.streaming.stream(title)
        subtitles = self.subtitles.enable_subtitles(title, language)
        return f"{movie}\n{streaming}\n{subtitles}"

@app.route('/watch/<title>')
def watch_movie(title):
    facade = MovieFacade()
    return facade.watch_movie(title)

if __name__ == "__main__":
    app.run(debug=True)
