# ============================================================
# JAZZMIN - Админ-панель с поддержкой переключения тем
# ============================================================

JAZZMIN_SETTINGS = {
    # ---------- Базовые настройки ----------
    "site_title": "GEEKS",
    "site_header": "GEEKS",
    "site_brand": "GEEKS",
    "site_logo": 'GEEKS',
    "login_logo": 'GEEKS',
    "login_logo_dark": 'GEEKS',
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Добро пожаловать в ПУ сайта",
    "copyright": "Acme Library Ltd",
    
    # ---------- Поиск ----------
    "search_model": ["auth.User", "auth.Group"],
    
    # ---------- Аватар пользователя ----------
    "user_avatar": None,
    
    # ---------- Верхнее меню ----------
    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "GitHub", "url": "https://github.com/farridav/django-jazzmin", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    
    # ---------- Меню пользователя ----------
    "usermenu_links": [
        {"name": "Поддержка", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    
    # ---------- Боковое меню ----------
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    
    "custom_links": {
        "books": [{
            "name": "Создать сообщения",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },
    
    # ---------- Иконки ----------
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    
    # ---------- Модальные окна ----------
    "related_modal_active": False,
    
    # ---------- UI настройки ----------
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": True,
    "show_theme_chooser": True,        # <-- ВКЛЮЧАЕТ ПЕРЕКЛЮЧАТЕЛЬ ТЕМ
    
    # ---------- Формы ----------
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible", 
        "auth.group": "vertical_tabs"
    },
    
    # ---------- Языки ----------
    "language_chooser": False,
}

# ============================================================
# JAZZMIN UI TWEAKS - Визуальные настройки (исправлено для v3+)
# ============================================================
JAZZMIN_UI_TWEAKS = {
    # ---------- Режим темы (ВАЖНО!) ----------
    "default_theme_mode": "auto",        # auto/dark/light - автоопределение по системе
    
    # ---------- Основная тема ----------
    "theme": "flatly",                    # Выбери любую: flatly, litera, lumen, minty, 
                                          # pulse, sandstone, simplex, spacelab, united, yeti
    
    # ---------- Текст ----------
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    
    # ---------- Цвета ----------
    "brand_colour": False,
    "accent": "accent-primary",
    
    # ---------- Навбар ----------
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": False,
    
    # ---------- Футер ----------
    "footer_fixed": True,
    
    # ---------- Сайдбар ----------
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    
    # ---------- Верстка ----------
    "layout_boxed": False,
    
    # ---------- Кнопки ----------
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    
    # ---------- Дополнительно ----------
    "actions_sticky_top": False
}