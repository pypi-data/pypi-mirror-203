from __future__ import annotations

from django.db import models
from edc_constants.choices import YES_NO
from edc_constants.constants import CHOL, DM, HIV, HTN
from edc_dx import get_diagnosis_labels

default_prompts = {
    HIV: "Has the patient ever tested <U>positive</U> for HIV infection?",
    DM: "Has the patient ever been diagnosed with Diabetes",
    HTN: "Has the patient ever been diagnosed with Hypertension",
    CHOL: "Has the patient ever been diagnosed with High Cholesterol",
}


def baseline_review_model_mixin_factory(prompts: dict[str, str] | None = None):
    prompts = prompts or default_prompts

    class AbstractModel(models.Model):
        class Meta:
            abstract = True

    opts = {}
    for dx in get_diagnosis_labels():
        opts.update(
            {
                f"{dx}_dx": models.CharField(
                    verbose_name=prompts.get(dx),
                    max_length=15,
                    choices=YES_NO,
                )
            }
        )

    for name, fld_cls in opts.items():
        AbstractModel.add_to_class(name, fld_cls)

    return AbstractModel
