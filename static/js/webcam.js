
            // capture camera and/or microphone
            navigator.mediaDevices.getUserMedia({ video: true, audio: true }).then(function(camera) {

                // preview camera during recording
                document.getElementById('myVideo').muted = true;
                document.getElementById('myVideo').srcObject = camera;
                document.getElementById("myVideo").style.display = "none";

                // recording configuration/hints/parameters
                var recordingHints = {
                    type: 'video'
                };
                
           //video element to stop the video feed
                       
                // initiating the recorder
                var recorder = RecordRTC(camera, recordingHints);

                // starting recording here
                recorder.startRecording();

                // auto stop recording after 42 seconds
                var milliSeconds = 42 * 1000;
                setTimeout(function() {

                    // stop recording
                    recorder.stopRecording(function() {
                        
                        // get recorded blob
                        var blob = recorder.getBlob();

                        // generating a random file name
                        var fileName = getFileName('webm');
                        //var fileName = "abc123.webm"

                        // we need to upload "File" --- not "Blob"
                        var fileObject = new File([blob], fileName, {
                            type: 'video/webm'
                        });

                        var formData = new FormData();

                        // recorded data
                        formData.append('video-blob', fileObject);

                        // file name
                        formData.append('videoSuyog', fileObject.name);

                        //document.getElementById('header').innerHTML = 'Uploading to PHP using jQuery.... file size: (' +  bytesToSize(fileObject.size) + ')';

                        var upload_url = 'http://127.0.0.1:5000/uploads';
                        // var upload_url = 'RecordRTC-to-PHP/save.php';

                        var upload_directory = upload_url;
                        // var upload_directory = 'RecordRTC-to-PHP/uploads/';

                        // upload using jQuery
                         
                        $.ajax({
                            url: upload_url, // replace with your own server URL
                            data: formData,
                            cache: false,
                            contentType: false,
                            processData: false,
                            type: 'POST',
                            success: function(response) {
                                if (response === 'success') {
                                    alert('successfully uploaded recorded blob');

                                    // file path on server
                                    //var fileDownloadURL = upload_directory + fileObject.name;

                                    // preview the uploaded file URL
                                    //document.getElementById('header').innerHTML = '<a href="' + fileDownloadURL + '" target="_blank">' + fileDownloadURL + '</a>';

                                    // preview uploaded file in a VIDEO element
                                    //document.getElementById('myVideo').srcObject = null;
                                    //document.getElementById('myVideo').src = fileDownloadURL;

                                    // open uploaded file in a new tab
                                    //window.open(fileDownloadURL);
                                } else {
                                    alert(response); // error/failure
                                }
                            }
                        });

                        // release camera
                        console.log("this is before camera stops")
                        document.getElementById('myVideo').srcObject = document.getElementById('myVideo').src = null;
                        camera.getTracks().forEach(function(track) {
                            console.log("this has stopped")
                            track.stop();
                        });

                    });

                }, milliSeconds);
            });

            // this function is used to generate random file name
            function getFileName(fileExtension) {
                var d = new Date();
                var year = d.getUTCFullYear();
                var month = d.getUTCMonth();
                var date = d.getUTCDate();
                return 'RecordRTC-' + year + month + date + '-' + getRandomString() + '.' + fileExtension;
            }

            function getRandomString() {
                if (window.crypto && window.crypto.getRandomValues && navigator.userAgent.indexOf('Safari') === -1) {
                    var a = window.crypto.getRandomValues(new Uint32Array(3)),
                        token = '';
                    for (var i = 0, l = a.length; i < l; i++) {
                        token += a[i].toString(36);
                    }
                    return token;
                } else {
                    return (Math.random() * new Date().getTime()).toString(36).replace(/\./g, '');
                }
            }
        