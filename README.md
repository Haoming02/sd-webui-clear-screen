# SD Webui Clear Screen
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), which adds a button `🆑` to clear the console window.

## How it Works
It adds a button that when clicked, fires `os.system('cls')` or `os.system('clear')` depending on your OS.

## But Why ?
Useful for benchmarking, or when you just want to clean the console ~~after the webui craps out tons of errors~~.