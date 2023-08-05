# Copyright 2020 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

from hond.logger import Logger
from elasticsearch import Elasticsearch


class ElasticSearch:
    """
    ElasticSearch Driver Class
    """

    def __init__(self, connection, index_name):
        """Inits elasticsearch"""
        self.logger = Logger().get_logger(__name__)
        self.client = Elasticsearch(connection)
        self.index_name = index_name

    def get_client(self):
        """
        Get elasticsearch client

        Returns:
            a dict of client info
        """
        return self.client.info()

    def migrate(self, shards=1, replicas=1):
        """
        Create metric index
        """
        doc = {
            "settings": {"number_of_shards": shards, "number_of_replicas": replicas},
            "mappings": {
                "properties": {
                    "id": {"type": "text"},
                    "name": {"type": "text"},
                    "value": {"type": "float"},
                    "timestamp": {"type": "long"},
                    "meta": {"type": "object"},
                }
            },
        }

        response = self.client.index(index=self.index_name, document=doc)

        return response

    def insert(self, metric):
        """
        Insert metrics into elastic search
        """
        doc = {
            "id": metric.id,
            "name": metric.name,
            "value": metric.value,
            "timestamp": metric.timestamp,
            "meta": metric.meta,
        }

        self.logger.debug("Insert metric into elasticsearch: {}", str(metric))

        response = self.client.index(index=self.index_name, document=doc)

        return response

    def is_absent(self, metric_name, for_in_sec=60):
        """
        Check if the metric is absent for x seconds
        """
        query = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response = self.search(query)

        return (
            response["hits"]["total"]["value"] == 0
            and len(response["hits"]["hits"]) == 0
        )

    def equal(self, metric_name, benchmark, for_in_sec=60):
        """
        Check if the metric is equal to the benchmark for x seconds
        """
        query1 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response1 = self.search(query1)

        # If no hits have been found
        if response1["hits"]["total"]["value"] == 0:
            return False

        query2 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {"match_phrase": {"value": {"query": benchmark}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response2 = self.search(query2)

        return (
            response1["hits"]["total"]["value"] == response2["hits"]["total"]["value"]
        )

    def above(self, metric_name, benchmark, for_in_sec=60):
        """
        Check if the metric is above the benchmark for x seconds
        """
        query1 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response1 = self.search(query1)

        # If no hits have been found
        if response1["hits"]["total"]["value"] == 0:
            return False

        query2 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {"range": {"value": {"gt": benchmark}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response2 = self.search(query2)

        return (
            response1["hits"]["total"]["value"] == response2["hits"]["total"]["value"]
        )

    def below(self, metric_name, benchmark, for_in_sec=60):
        """
        Check if the metric is below the benchmark for x seconds
        """
        query1 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response1 = self.search(query1)

        # If no hits have been found
        if response1["hits"]["total"]["value"] == 0:
            return False

        query2 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {"range": {"value": {"lt": benchmark}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response2 = self.search(query2)

        return (
            response1["hits"]["total"]["value"] == response2["hits"]["total"]["value"]
        )

    def above_equal(self, metric_name, benchmark, for_in_sec=60):
        """
        Check if the metric is above or equal the benchmark for x seconds
        """
        query1 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response1 = self.search(query1)

        # If no hits have been found
        if response1["hits"]["total"]["value"] == 0:
            return False

        query2 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {"range": {"value": {"gte": benchmark}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response2 = self.search(query2)

        return (
            response1["hits"]["total"]["value"] == response2["hits"]["total"]["value"]
        )

    def below_equal(self, metric_name, benchmark, for_in_sec=60):
        """
        Check if the metric is below or equal the benchmark for x seconds
        """
        query1 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response1 = self.search(query1)

        # If no hits have been found
        if response1["hits"]["total"]["value"] == 0:
            return False

        query2 = {
            "query": {
                "bool": {
                    "must": [
                        {"match_phrase": {"name": {"query": metric_name}}},
                        {"range": {"value": {"lte": benchmark}}},
                        {
                            "range": {
                                "timestamp": {"gte": int(time.time()) - for_in_sec}
                            }
                        },
                    ]
                }
            }
        }

        response2 = self.search(query2)

        return (
            response1["hits"]["total"]["value"] == response2["hits"]["total"]["value"]
        )

    def search(self, query):
        """
        Query elasticsearch index
        """
        return self.client.search(index=self.index_name, body=query)

    def evaluate(expression):
        """
        Evaluate a trigger value

        Examples:
            m{customers.123.456.789.cpu>=20}[30s]
            m{customers.123.456.789.cpu<20}[30s]
            m{customers.123.456.789.cpu==nul}[30s]
            m{customers.123.456.789.cpu==nul}[30s] and m{customers.123.456.789.mem==nul}[30s]

        TODO: switch to safer way other than eval but right now triggers is not a user input
        """
        result = []
        expressions = re.split(" and | or ", expression)

        for exp in expressions:
            pattern = r"^(m)\{(.*)\}(\[(.*)\])?$"
            match = re.match(pattern, exp)
            if match:
                items = re.split(">=|<=|==|>|<", match.group(2))

                if items[1] == "nul":
                    metric_name = items[0]
                    for_in_sec = int(match.group(4))

                    value = self.is_absent(metric_name, for_in_sec)
                else:
                    metric_name = items[0]
                    benchmark = float(items[1])
                    for_in_sec = int(match.group(4))

                    if "==" in match.group(2):
                        value = self.equal(self, metric_name, benchmark, for_in_sec)
                    elif ">=" in match.group(2):
                        value = self.above_equal(
                            self, metric_name, benchmark, for_in_sec
                        )
                    elif "<=" in match.group(2):
                        value = self.below_equal(
                            self, metric_name, benchmark, for_in_sec
                        )
                    elif ">" in match.group(2):
                        value = self.above(self, metric_name, benchmark, for_in_sec)
                    elif "<" in match.group(2):
                        value = self.below(self, metric_name, benchmark, for_in_sec)

                if value:
                    result.append("True")
                else:
                    result.append("False")
            else:
                raise Exception("Invalid expression: {}".format(exp))

        out = expression

        for i in range(len(expressions)):
            out = out.replace(expressions[i], result[i])

        return eval(out)
