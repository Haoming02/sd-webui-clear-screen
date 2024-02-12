onUiLoaded(async () => {
    const container = document.getElementById('quicksettings');
    const btn = document.getElementById('cls_btn');
    btn.classList.add('tool');
    container.appendChild(btn);
});
