// Keep playback focused on the selected work.
document.querySelectorAll("video").forEach((selected) => {
  selected.addEventListener("play", () => {
    document.querySelectorAll("video").forEach((other) => {
      if (other !== selected) other.pause();
    });
  });
});
