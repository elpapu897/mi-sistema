#!/usr/bin/env bash
systemctl --user restart hermes-gateway.service
systemctl --user is-active hermes-gateway.service
