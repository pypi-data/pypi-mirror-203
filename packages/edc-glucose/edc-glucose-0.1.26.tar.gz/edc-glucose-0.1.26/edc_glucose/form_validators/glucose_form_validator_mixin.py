from edc_constants.constants import YES

from ..utils import validate_glucose_as_millimoles_per_liter


class GlucoseFormValidatorMixin:
    fasting_fld = "fasting"

    def validate_glucose_test(self) -> None:
        self.required_if(YES, field="glucose_performed", field_required="glucose_date")
        self.required_if(YES, field="glucose_performed", field_required=self.fasting_fld)
        self.required_if(YES, field="glucose_performed", field_required="glucose_value")
        validate_glucose_as_millimoles_per_liter("glucose", self.cleaned_data)
        self.required_if(YES, field="glucose_performed", field_required="glucose_quantifier")
        self.required_if(YES, field="glucose_performed", field_required="glucose_units")
