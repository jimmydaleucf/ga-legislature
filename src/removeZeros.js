let paths = document.querySelectorAll("path");
for (i = 0; i < paths.length; i++) {
  let id = paths[i].getAttribute("id");
  const modId = id.replace(/^0+/, "");
  console.log(modId);
  paths[i].setAttribute("id", modId);
}
