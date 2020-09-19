def get_form_data(factory, form) -> dict:
    gastro = factory.build()
    return {field_name: getattr(gastro, field_name) for field_name in form.Meta.fields}


def create_gastro_form_data(factory, form) -> dict:
    data = get_form_data(factory=factory, form=form)
    data["handicapped_accessible"] = ""
    data["handicapped_accessible_wc"] = ""
    data["dog"] = ""
    data["organic"] = ""
    data["wlan"] = ""
    data["brunch"] = ""
    data["gluten_free"] = ""
    data["child_chair"] = ""
    data["catering"] = ""
    data["breakfast"] = ""
    data["delivery"] = ""
    return data
