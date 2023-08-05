from marshmallow import fields, post_load
from skatepark.schemas import StepSchema, PolymorphicSchema


class PromptStepSchema(StepSchema):
    prompt_template = fields.Str(required=True)
    context = fields.Dict(keys=fields.Str(), values=fields.Raw())
    driver = fields.Nested(PolymorphicSchema(), allow_none=True)

    @post_load
    def make_obj(self, data, **kwargs):
        from skatepark.steps import PromptStep

        return PromptStep(**data)
