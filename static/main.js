const clouds = document.querySelector(".clouds");

window.addEventListener("scroll", () => {
  const win = window.pageYOffset;

  if (win > 2280) {
    clouds.style.height = 146 - +win / 50 + "%";
  }
});
