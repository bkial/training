<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>session report</h1>
    % for session in objects:
        <h2>${session.course_id.name} - ${session.name}</h2>
        <p>From ${formatLang(session.date_debut,date=True)}to
        ${formatLang(session.date_fin,date=True)}.</p>
        <p>Attendees:
        <ul>
            %for att in session.participants:
            <li>${att.name}</li>
            %endfor
        </ul>
        </p>
    % endfor
</body>
</html>