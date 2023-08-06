# SPDX-FileCopyrightText: 2023 Susumu OTA <1632335+susumuota@users.noreply.github.com>
# SPDX-License-Identifier: MIT

from __future__ import annotations

from nanoatp import BskyAgent


class RichText:
    def __init__(self) -> None:
        self.text = ""
        self.facets = []
        pass

    def detectFacets(self, agent: BskyAgent) -> list:
        return []

    def __str__(self) -> str:
        return self.text

    def __len__(self) -> int:
        return len(self.text)
