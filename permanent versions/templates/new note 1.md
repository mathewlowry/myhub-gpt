---
creation date: <% tp.file.creation_date() %>
modification date: <% tp.file.last_modified_date("DDDD MMMM YYYY HH:mm:ss") %>
<%* 
let title = tp.file.title 
if (title.startsWith("Untitled")) { 
title = await tp.system.prompt("Title"); 
} 
await tp.file.rename(`${title}`); 
tR += "---" 
%>
# <%* tR += `${title}` %>, created # <% tp.file.creation_date() %>
<% tp.file.cursor() %>


