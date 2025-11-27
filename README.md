# India Mandi Price Analytics System

A production-grade data engineering project analyzing agricultural wholesale market prices across India's 1,800+ regulated mandis.

## 📋 Project Overview

This project builds an end-to-end data pipeline that ingests daily mandi price data from government APIs, transforms it through multiple layers, and produces analytics-ready tables for price analysis, regional comparison, and trend identification.

**Why this project?**
- **Unique domain**: Rarely seen in data engineering portfolios
- **Real messiness**: Handles actual government data inconsistencies (naming, units, dates)
- **Production patterns**: Demonstrates scheduling, orchestration, monitoring, and testing
- **Clear business value**: Solves a real problem for farmers, traders, and policymakers

## 🏗️ Architecture

The project follows the **Medallion Architecture** pattern: