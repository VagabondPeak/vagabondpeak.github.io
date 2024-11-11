<script>
    // Function to preview the uploaded image
    function previewImage(event) {
        const file = event.target.files[0];
        if (file) {
            const fileType = file.type.split('/')[0];
            if (fileType !== 'image') {
                alert('Please upload an image file.');
                return;
            }
            const reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('profilePic').src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    }
</script>

</body>
</html>
