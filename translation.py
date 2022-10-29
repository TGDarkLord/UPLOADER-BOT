class Translation(object):

    ERROR = "<b>ERROR :</b> {}"

    START_TEXT = """<b><i>Hello 👋 {},\n\nI'm URL Uploader Bot!\nYou Can Upload HTTP/HTTPS Direct Link, Using This Bot.\n\n/help For More Details</b></i>"""

    FORMAT_SELECTION = "Select The Desired Format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."

    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | Filename | Username | Password"""
    DOWNLOAD_START = "📥 Downloading..."
    UPLOAD_START = "📤 Uploading..."
    RCHD_TG_API_LIMIT = "Downloaded In {} Seconds.\nDetected File Size: {}\nSorry, But I Cannot Upload Files Greater Than 2GB Due To Telegram API Limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks For Using @TechUrlUploader_Bot\n\n<b>Join : @Tech_Projects2019</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded In {} Seconds.\nUploaded In {} Seconds."
    SAVED_CUSTOM_THUMB_NAIL = "Custom Video/File Thumbnail Saved. This Image Will Be Used In The Video/File."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom Thumbnail Deleted Successfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> Said: {}"
    HELP_USER = """How To Use Me? Follow These Steps!
    
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

If Bot Didn't Respond, Contact @TechprojectsChat"""

    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail To A Media Album, To Generate Custom Thumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album Should Contain Only Two Photos. Please Re-send The Media Album, And Then Try Again Or Send Only Two Photos In An Album."
You Can Use /rename Command After Receiving File To Rename It With Custom Thumbnail Support."""

    CANCEL_STR = "✔️ Process  Successfully Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} Files In {} Seconds."
    SLOW_URL_DECED = "Gosh That Seems To Be A Very Slow URL. Since You Were Screwing My Home, I Am In No Mood To Download This File. Meanwhile, Why Don't You Try This:==> https://shrtz.me/PtsVnf6 And Get Me A Fast URL So That I Can Upload To Telegram, Without Me Slowing Down For Other Users."

    ERROR_YTDLP = "Please Report This Issue On https://yt-dl.org/bug. Make Sure You Are Using The Latest Version; See ===>> https://yt-dl.org/update On How To Update. Be Sure To Call YouTube-Dl With The Verbose Flag And Include Its Complete Output."
