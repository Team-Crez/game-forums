self.addEventListener('fetch', function(event) {
    console.log('Fetch!', event.request);
});