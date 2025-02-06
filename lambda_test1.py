def handler(event, context):
    name = event.get("name", "Anonymous")
    weather = event.get("weather", "unknown")

    return {
        'statusCode': 200,
        'body': f"Hi {name}, hello from Lambda. It is {weather} today.",
         'event': f'{event}',
         'context': f'{context}' 
    }

