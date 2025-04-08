# Copyright (c) 2024 Snowflake Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import sys

from common import print_hello
#from first_snowpark_project.app.common import print_hello
from snowflake.snowpark import Session




def hello_procedure(session: Session, name: str) -> str:
    return print_hello(name)
    #return "Test procedure"


def test_procedure(session: Session) -> str:
    return "Test procedure"

def test_procedure_two(session: Session) -> str:
    return "Test procedure"

def execute_sql_statements(session: Session) -> None:
    session.sql("EXECUTE IMMEDIATE FROM @dev_deployment/my_snowpark_project/test.sql").collect()

# For local debugging
# Beware you may need to type-convert arguments if you add input parameters
if __name__ == "__main__":
    # Create a local Snowpark session
    with Session.builder.config("local_testing", True).getOrCreate() as session:
        print(hello_procedure(session, *sys.argv[1:]))  # type: ignore