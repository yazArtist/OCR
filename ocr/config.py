#dynaconf kullan
from ocr.enums import DataTypes, Countries

data_patterns = {
    DataTypes.PHONE_NUMBER: r'\b\d{10}\b',
    DataTypes.ID_NUMBER: r'\b\d{9}\b',
    DataTypes.CREDIT_CARD_NUMBER: r'\b\d{4}-\d{4}-\d{4}-\d{4}\b',
    DataTypes.PLATE: r'\b[A-Z\d]{2}-[A-Z\d]{2}-[A-Z\d]{2}\b',
    DataTypes.DATE: r'(?<!\d)(?:(?:0?[1-9]|1[0-2])\/(?:0?[1-9]|[12]\d|3[01])\/(?:19|20)\d{2})(?!\d)',
    DataTypes.EMAIL: r'\b[\w.-]+@[\w.-]+\b',
    DataTypes.DOMAIN: r'([a-z]{1,2}tps?):\/\/((?:(?!(?:\/|#|\?|&)).)+)(?:(\/(?:(?:(?!(?:#|\?|&)).)+\/))?)(?:(?:(?!(?:\.|$|\?|#)).)+)?(?:\.(?:(?!(?:\?|$|#)).)+)?(?:(\?(?:(?!(?:$|#)).)+))?(?:(#.+))?',
    DataTypes.URL: r'\bhttps?://[\w./-]+\b',
    DataTypes.HASH: r'\b[A-Fa-f\d]{32}\b'
}

country_patterns = {
    Countries.TURKEY: r'\b\d{11}\b',
    Countries.GERMANY: r'\b\d{9}\b',
    Countries.FRANCE: r'\b\d{12}\b',
    Countries.UK: r'\b\d{9}\b',
    Countries.ITALY: r'\b\d{10}\b',
    Countries.SPAIN: r'\b\d{9}\b',
}

phone_number_regex = r'\b\d{3}[-\s]?\d{3}[-\s]?\d{4}\b'
plate_number_regex = r'^[A-Z\d]{1,3}\d{1,4}[A-Z\d]{1,3}$'
url_pattern_regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+|(?:www\.[-\w]+\.[-\w]+)'
credit_card_number_regex = r'\b\d{4}-\d{4}-\d{4}-\d{4}\b'
