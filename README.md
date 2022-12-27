# Text-in-Picture
<h2>Welcome!</h2>
This tool can be used to hide messages in images without changing the image as far as the human eye can see.</br>
<strong>WARNING - The message is not encrypted and can be read by anyone who gets the image using this tool! Do NOT use for sensitive info!</strong>

<h3>Setup and use</h3>
<h5>Pre-requisites:</h5>
<ul><li>Python 3 (written in 3.9 & 10 so these are known to work)</li></ul></br>
<h5>To use this tool, follow these steps:</h5>
<ol><li>Clone this repository to your device.</li><li>Move into the cloned project.</li><li>Run pictureEncrypt.pyw by typing ```python pictureEncrypt.pyw``` or double clicking on theFile</li>
<li>To encrypt an image, type your message in the top text box and then click Encrypt</li>
<li>Choose an image file to use to hide a message. <strong>This won't affect the file, it will create a copy!</strong></li>
<li>Your message in a picture will be in the same folder as the python files and will be called ```<current date>.png```. Feel free to rename!</li>
<li>To decrypt an image, click the decrypt button and select the file you wish to decrypt.</li>
<li>Your message will show up in the bottom text box and can be scrolled through. Most of the message will be a load of random symbols as not all the pixels were used to hide the message but all the pixels are decrypted</li>
</ol>

Sadly this only works in English at the moment but if you want to add other language support, feel free to do a pull request!
