#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import random
import sys
import traceback
from pathlib import Path

###############################################################################

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)4s: %(module)s:%(lineno)4s %(asctime)s] %(message)s",
)
log = logging.getLogger(__name__)

###############################################################################


DEFAULT_OUTPUT_FILE = Path("factorial-vignettes.txt")
VIGNETTE_TEMPLATE = """
**{Creator}** has created a dataset comprised of millions of public Tweets from thousands of Twitter users. This dataset was created using the **{AcquisitionMethod}**. This dataset was originally published **{Recency}** and **{Adoption}**.

The use of this dataset by a **{User}** in developing a chat bot for **{Usage}** would concern me.
""".strip()


class Factors:
    class Creator:
        UniversityResearchTeam = "A university research team"
        IndustryResearchTeam = "A commercial research team"

    class AcquisitionMethod:
        Scraped = "Twitter API"
        ScrapedWithInforming = (
            "Twitter API and the development team asked each user if they could "
            "use their Tweets in the dataset"
        )
        ScrapedWithoutInforming = (
            "Twitter API but the development team did not ask each user if they "
            "could use their Tweets in the dataset"
        )

    class Recency:
        TwoYears = "two years ago"
        FiveYears = "five years ago"
        TenYears = "ten years ago"

    class Adoption:
        HighlyAdopted = (
            "has been used by more than 25 other research teams and companies"
        )
        ModeratelyAdopted = (
            "has been used by more than 10 other research teams and companies"
        )
        MinimallyAdopted = "hasn't been used by any research team or company yet"

    class User:
        Student = "student / intern"
        Researcher = "researcher"
        Company = "company"

    class Usage:
        Learning = "education and learning"
        Application = "use in a larger commercial application"


FactorsList = [attr for attr in dir(Factors) if "__" not in attr]


###############################################################################


class Args(argparse.Namespace):
    def __init__(self) -> None:
        self.__parse()

    def __parse(self) -> None:
        p = argparse.ArgumentParser(
            prog="generate-lcd-vignettes",
            description=(
                "Generate multiple Long Tail of Controversial Dataset "
                "factorial vignettes."
            ),
        )
        p.add_argument(
            "-n",
            type=int,
            default=10,
            dest="n",
            help="Number of factorial vignettes to generate.",
        )
        p.add_argument(
            "-d",
            "--dst",
            type=Path,
            default=DEFAULT_OUTPUT_FILE,
            dest="dst",
            help="Storage path for generated factorial vignettes file.",
        )
        p.add_argument(
            "--overwrite",
            action="store_true",
            dest="overwrite",
            help=(
                "If there is an existing file at the destination, "
                "should it be overwritten."
            ),
        )

        p.parse_args(namespace=self)


###############################################################################


def _gen_vignettes(
    n: int = 10,
    dst: Path = DEFAULT_OUTPUT_FILE,
    overwrite: bool = False,
) -> Path:
    # We don't want to overwrite existing vignettes unless explicit
    if dst.exists() and not overwrite:
        raise FileExistsError(dst)

    # Generate list of vignettes
    vignettes = []
    for i in range(n):
        # Get random choices for each factor
        choices = {}
        for factor_name in FactorsList:
            factor = getattr(Factors, factor_name)
            options = [
                getattr(factor, attr) for attr in dir(factor) if "__" not in attr
            ]
            choices[factor_name] = random.choice(options)

        # Fill vignette and append
        vignettes.append(VIGNETTE_TEMPLATE.format(**choices))

    # Compile to single string with line breaks
    lb = "-" * 80
    compiled = f"\n\n{lb}\n\n".join(vignettes)

    # Store
    with open(dst, "w") as open_f:
        open_f.write(compiled)


def main() -> None:
    try:
        args = Args()
        _gen_vignettes(
            n=args.n,
            dst=args.dst,
            overwrite=args.overwrite,
        )
    except Exception as e:
        log.error("=============================================")
        log.error("\n\n" + traceback.format_exc())
        log.error("=============================================")
        log.error("\n\n" + str(e) + "\n")
        log.error("=============================================")
        sys.exit(1)


###############################################################################
# Allow caller to directly run this module (usually in development scenarios)

if __name__ == "__main__":
    main()
