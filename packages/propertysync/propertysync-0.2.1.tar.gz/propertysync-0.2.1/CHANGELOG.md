# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
### Fixed
### Changed
### Removed

## [0.2.1] - 2023-04-26

### Added
- Added optional save_to_search and wait_time parameters to create_batch_from_json method that allows you to submit a batch, wait for it's documents to be processed and save the batch to search making those documents live in the plant.

### Fixed
- Corrected package requirements

## [0.1.0] - 2023-04-25

### Added
- Added instrument_numbers method to Batch class to return a list of instrument numbers
- Add govLot to acreage searches
- Added package specific documentation

### Fixed
- Fixes to subdivision searches
- Fix trailing slashes when using non-default indexing and/or search urls

## [0.0.4] - 2023-03-26

### Added
- First release to PyPi

### Changed
- Updated project to use hatch for build and publishing
