# Concrete design questions

These examples are fictional. They illustrate decisions, not fixed recipes or descriptions of the user's repository.

## Immutable order data

`OrderSnapshot` stores a list of `OrderLine` values.

A read-only reference to the list does not necessarily prevent list mutation. A read-only view can reflect changes to the original list. A shallow copy can still share mutable `OrderLine` values. Check the actual guarantees of the target language and collection type.

Ask whether the contract requires a stable snapshot or a live view. For a stable snapshot, copy the collection and make its elements immutable or copy them as needed. Follow project rules for missing elements. Do not choose a copying API without checking those rules.

## Shared state in a service

`InventoryService` checks available stock and then reserves stock.

A thread-safe map does not make those two steps atomic. Identify the invariant and the actual owner of stock. If several replicas share the same database state, an in-process lock alone cannot protect the cross-replica invariant.

Choose an existing transactional, atomic-update, or coordination mechanism that fits the storage contract. Verify that two simultaneous requests cannot both reserve the same stock when that would violate the contract.

## Retrying a remote write

`PaymentClient` sends a charge request. The response times out.

The timeout does not establish whether the payment provider charged the account. Before retrying, inspect the provider's idempotency contract and the existing client policy. A request ID alone does not prevent duplicates unless the provider or storage enforces the required deduplication behavior.

Define the key's reuse across attempts, the applicable lifetime, retryable outcomes, total attempts, and deadline. If the required semantics are unavailable, report the unresolved decision instead of inventing a retry policy.

## Authorization and cache

`DocumentService` receives an authorization denial when fetching a document.

Returning a cached document is not automatically an acceptable fallback. The cache may contain data that the current user can no longer access. Check the required access and freshness rules. Preserve denial unless the established contract explicitly supports a different authorized result.

## A meaningful abstraction

Two functions both load a record and send an event. Their transaction and error contracts differ.

Similar code shape does not justify a generic load-and-publish framework. Keep the flows separate unless a shared domain contract exists. Extract the part that has the same meaning, if that reduces complexity without hiding the two effect contracts.
