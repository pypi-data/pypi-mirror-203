# Copyright (C) 2022 Anthony Harrison
# SPDX-License-Identifier: Apache-2.0

from sbommerge.cyclonedxgenerator import CycloneDXGenerator
from sbommerge.spdxgenerator import SPDXGenerator


class SBOMGenerator:
    """
    Simple SBOM Generator.
    """

    def __init__(self, include_license: False, sbom_type="spdx", format="tag", application="sbom4python", version="0.1", package_manager = "pypi"):
        if sbom_type == "spdx":
            self.bom = SPDXGenerator(include_license, format, application, version)
            self.bom.set_purl(package_manager)
        else:
            self.bom = CycloneDXGenerator(include_license, format, application, version)
            self.bom.set_purl(package_manager)

    def generate_spdx(self, project_name, packages, files=None):
        self.sbom_complete = False
        project_id = self.bom.generateDocumentHeader(project_name)
        # Process list of files
        if files is not None:
            id = 1
            relationship = " CONTAINS "
            for file in files:
                self.bom.generateFileDetails(
                    file["name"],
                    str(id) + "-" + file["name"],
                    file,
                    project_id,
                    relationship,
                )
                id = id + 1
        id = 1
        package_set = {}
        for package in packages:
            #print (package)
            product = package["name"]
            #parent = package[0].lower()
            parent = "-"
            if product not in package_set:
                package_set[product] = str(id) + "-" + product
                if parent == "-":
                    parent_id = project_id
                    relationship = " DESCRIBES "
                else:
                    if parent in package_set:
                        parent_id = package_set[parent]
                        relationship = " CONTAINS "
                self.bom.generatePackageDetails(
                    product,
                    str(id) + "-" + product,
                    package,
                    parent_id,
                    relationship,
                )
                id = id + 1
            else:
                if parent == "-":
                    parent_id = project_id
                    relationship = " DESCRIBES "
                elif parent in package_set:
                    relationship = " CONTAINS "
                    parent_id = package_set[parent]
                else:
                    parent_id = None
                if parent_id is not None:
                    self.bom.generateRelationship(
                        self.bom.package_ident(parent_id),
                        self.bom.package_ident(package_set[product]),
                        relationship,
                    )

    def get_spdx(self):
        if not self.sbom_complete:
            self.bom.showRelationship()
            self.sbom_complete = True
        return self.bom.getBOM()

    def get_relationships(self):
        return self.bom.getRelationships()

    def get_cyclonedx(self):
        return self.bom.getBOM()

    def generate_cyclonedx(self, project_name, packages):
        self.bom.generateDocumentHeader(project_name)
        # Process list of packages
        id = 1
        package_set = {}
        for package in packages:
            product = package["name"]
            #parent = package[0].lower()
            parent = "-"
            if product not in package_set:
                package_set[product] = str(id) + "-" + product
                if parent == "-":
                    type = "application"
                else:
                    type = "library"
                self.bom.generateComponent(
                    package_set[product], type, package
                )
                if parent != "-":
                    self.bom.generateRelationship(
                        package_set[parent], package_set[product]
                    )
                id = id + 1
