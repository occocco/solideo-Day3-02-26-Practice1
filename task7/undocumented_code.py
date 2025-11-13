def validate_korean_id(id_number):
    if len(id_number) != 13:
        return False
    return True

def mask_sensitive_data(text, pattern):
    import re
    return re.sub(pattern, '***', text)
