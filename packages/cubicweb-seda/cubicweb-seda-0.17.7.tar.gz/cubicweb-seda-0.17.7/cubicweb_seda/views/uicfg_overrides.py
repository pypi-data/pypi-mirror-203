# -*- coding: utf-8 -*-
#
# Copyright © LOGILAB S.A. (Paris, FRANCE) 2016-2021
# Contact http://www.logilab.fr -- mailto:contact@logilab.fr
#
# This software is governed by the CeCILL-C license under French law and
# abiding by the rules of distribution of free software. You can use,
# modify and/ or redistribute the software under the terms of the CeCILL-C
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty and the software's author, the holder of the
# economic rights, and the successive licensors have only limited liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading, using, modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean that it is complicated to manipulate, and that also
# therefore means that it is reserved for developers and experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systemsand/or
# data to be ensured and, more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL-C license and that you accept its terms.
#
"""THIS FILE IS NOT GENERATED FROM SEDA XSD FILES, IT CAN BE EDITED"""

from cubicweb.web.views import uicfg

pvs = uicfg.primaryview_section
abaa = uicfg.actionbox_appearsin_addmenu
affk = uicfg.autoform_field_kwargs
afs = uicfg.autoform_section

# cubicweb_eac


# form

afs.tag_subject_of(("AuthorityRecord", "languages", "*"), "main", "hidden")
afs.tag_subject_of(("AuthorityRecord", "record_id", "*"), "main", "hidden")

for attribute in ("authorized_form", "preferred_form", "alternative_form",
                  "language", "script_code"):
    afs.tag_subject_of(("NameEntry", attribute, "*"), "main", "hidden")

for objrel in ("convention_of", "parallel_names_of", "resource_relation_resource",
               "family_from", "family_to",
               "function_relation_agent", "function_relation_function",
               "identity_from", "identity_to"):
    afs.tag_object_of(("*", objrel, "AuthorityRecord"), "main", "hidden")
