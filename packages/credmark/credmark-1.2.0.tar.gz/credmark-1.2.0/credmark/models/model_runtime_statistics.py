from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelRuntimeStatistics")


@attr.s(auto_attribs=True)
class ModelRuntimeStatistics:
    """
    Attributes:
        slug (str): Short identifying name for the model Example: var.
        version (str): Version of the model Example: 1.0.
        min (float): Minimum model runtime in milliseconds
        max (float): Maximum model runtime in milliseconds
        mean (float): Mean (average) model runtime in milliseconds
        median (float): Median model runtime in milliseconds
    """

    slug: str
    version: str
    min: float
    max: float
    mean: float
    median: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slug = self.slug
        version = self.version
        min = self.min
        max = self.max
        mean = self.mean
        median = self.median

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "version": version,
                "min": min,
                "max": max,
                "mean": mean,
                "median": median,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slug = d.pop("slug")

        version = d.pop("version")

        min = d.pop("min")

        max = d.pop("max")

        mean = d.pop("mean")

        median = d.pop("median")

        model_runtime_statistics = cls(
            slug=slug,
            version=version,
            min=min,
            max=max,
            mean=mean,
            median=median,
        )

        model_runtime_statistics.additional_properties = d
        return model_runtime_statistics

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
